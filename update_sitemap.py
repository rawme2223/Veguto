import os
from datetime import date

sitemap_path = 'sitemap.xml'
games_dir = 'games'
base_url = 'https://veguto.rawme.online/games/'
today = date.today().strftime('%Y-%m-%d')

# قراءة الملف الحالي
with open(sitemap_path, 'r') as f:
    lines = f.readlines()

# استخراج الروابط الموجودة فعلاً لتجنب التكرار
existing_locs = [line.split('<loc>')[1].split('</loc>')[0] for line in lines if '<loc>' in line]

new_entries = []
# مسح المجلد بحثاً عن ألعاب جديدة
for game_name in os.listdir(games_dir):
    game_path = os.path.join(games_dir, game_name)
    if os.path.isdir(game_path):
        url = f"{base_url}{game_name}/about"
        if url not in existing_locs:
            entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.80</priority>
  </url>\n"""
            new_entries.append(entry)

# إذا وجدت ألعاب جديدة، أضفها قبل إغلاق الوسم </urlset>
if new_entries:
    lines.insert(-1, "".join(new_entries))
    with open(sitemap_path, 'w') as f:
        f.writelines(lines)
    print(f"Added {len(new_entries)} new game links to sitemap.")
else:
    print("No new games found.")
