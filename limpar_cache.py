"""
limpar_cache.py
---------------
Remove do article_cache.json entradas com imagens genéricas/contaminadas,
forçando o app a re-fetch das imagens reais na próxima execução.

Padrões removidos:
- Banners do Hellenic Shipping News (best_oasis_banner, hnn_banner, /2014/, /2015/, /2016/)
- Logos/tops do Petronotícias (pn-topo, /2017/04/, bannertopo, /themes/)
- Padrões genéricos universais (placeholder, logo.png, etc.)
"""

import json
import os
import re
from datetime import datetime, timezone

CACHE_FILE = "output/article_cache.json"
BACKUP_FILE = "output/article_cache.backup.json"

GENERIC_IMAGE_PATTERNS = [
    # Petronotícias
    "petronoticias.com.br/wp-content/uploads/2017/04/pn-topo",
    "petronoticias.com.br/wp-content/uploads/2017/04/",
    "petronoticias.com.br/wp-content/uploads/2026/02/bannertopo",
    "petronoticias.com.br/wp-content/uploads/2016/03/",   # logo-ebco e outros ativos antigos
    "petronoticias.com.br/wp-content/themes/",
    # Hellenic Shipping News
    "hellenicshippingnews.com/wp-content/uploads/2014/",
    "hellenicshippingnews.com/wp-content/uploads/2015/",
    "hellenicshippingnews.com/wp-content/uploads/2016/",
    "hellenicshippingnews.com/wp-content/themes/",
    "best_oasis_banner",
    "hnn_banner",
    # Universais
    "/default-image", "/placeholder", "/no-image", "/sem-imagem",
    "ico-time.png", "ico-comment.png",
    "logo.png", "/img/logo", "fallbackimage.jpg",
]


def is_generic_image(url):
    if not url:
        return False
    low = url.lower()
    return any(pat.lower() in low for pat in GENERIC_IMAGE_PATTERNS)


def main():
    if not os.path.exists(CACHE_FILE):
        print(f"Cache não encontrado: {CACHE_FILE}")
        return

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    total = len(cache)

    # Backup antes de modificar
    with open(BACKUP_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    print(f"Backup salvo em: {BACKUP_FILE}")

    cleared_image = 0
    for url, entry in cache.items():
        img = entry.get("image_url") or ""
        if is_generic_image(img):
            entry["image_url"] = None
            cleared_image += 1
            print(f"  [imagem limpa] {url[:80]}")
            print(f"    era: {img[:100]}")

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Concluído — {total} entradas no cache, {cleared_image} imagens contaminadas limpas.")
    print("Na próxima execução do app, o sistema vai re-fetchar as imagens reais.")


if __name__ == "__main__":
    main()
