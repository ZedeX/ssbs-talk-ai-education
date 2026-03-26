import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_content = '''            &lt;div class="final-item"&gt;
              &lt;span class="final-item-icon"&gt;💬&lt;/span&gt;
              &lt;div class="final-item-text"&gt;欢迎任何关于AI与家庭教育的交流和提问&lt;/div&gt;
            &lt;/div&gt;
          &lt;/div&gt;'''

new_content = '''            &lt;div class="final-item"&gt;
              &lt;span class="final-item-icon"&gt;💬&lt;/span&gt;
              &lt;div class="final-item-text"&gt;欢迎任何关于AI与家庭教育的交流和提问&lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="final-item"&gt;
              &lt;span class="final-item-icon"&gt;📂&lt;/span&gt;
              &lt;div class="final-item-text"&gt;&lt;strong&gt;&lt;a href="https://github.com/ZedeX/ssbs-talk-ai-education" target="_blank"&gt;GitHub 项目地址&lt;/a&gt;&lt;/strong&gt;（欢迎 Star &amp; Fork）&lt;/div&gt;
            &lt;/div&gt;
          &lt;/div&gt;'''

content = content.replace(old_content, new_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('GitHub link added successfully')
