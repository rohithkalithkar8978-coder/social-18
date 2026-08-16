python3 -m http.server 8080
pip3 install flask
python3 app.py
fuser -k 8080/tcp
python3 -m http.server 8080
python3 app.py
:root {
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
}
#canvas3d { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -2; }
.bg-overlay {
}
/* Navbar */
.navbar {
}
.logo { font-size: 1.2rem; font-weight: 600; letter-spacing: -0.5px; }
.logo span { color: var(--text-secondary); }
.nav-tag { font-size: 0.85rem; color: var(--text-secondary); font-weight: 400; }
.btn-apple {
}
.btn-apple:hover { opacity: 0.9; transform: scale(1.02); }
/* Main Content */
.content { text-align: center; padding: 120px 5% 60px; max-width: 1100px; margin: 0 auto; }
.eyebrow { color: var(--apple-accent); font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 0.5rem; }
.hero-title h1 {
}
.hero-title p { color: var(--text-secondary); font-size: 1.25rem; max-width: 650px; margin: 0 auto 3rem; font-weight: 400; line-height: 1.4; }
/* Grid Selector */
.sports-grid { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-bottom: 3rem; }
.sport-card {
}
.sport-card:hover {
}
.sport-num { font-size: 0.75rem; color: var(--text-secondary); font-weight: 600; margin-bottom: 0.3rem; }
.sport-name { font-size: 1.1rem; font-weight: 500; letter-spacing: -0.3px; }
/* Apple Spec Sheet Modal */
.details-card {
}
@keyframes fadeIn {
}
.hidden { display: none; }
.close-btn { position: absolute; top: 24px; right: 24px; background: rgba(255, 255, 255, 0.1); border: none; color: var(--text-secondary); width: 32px; height: 32px; border-radius: 50%; cursor: pointer; font-size: 0.9rem; }
.close-btn:hover { color: #fff; background: rgba(255, 255, 255, 0.2); }
.details-header h2 { font-size: 2.5rem; font-weight: 600; letter-spacing: -1px; margin-bottom: 2rem; }
.specs-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
.spec-box { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.5rem; border-radius: 16px; }
.spec-box.full-width { grid-column: span 2; }
.spec-box h4 { font-size: 0.95rem; color: var(--text-secondary); font-weight: 500; margin-bottom: 0.8rem; }
.spec-box p, .spec-box ul { font-size: 1.05rem; color: var(--text-primary); line-height: 1.5; font-weight: 400; }
.spec-box ul { list-style-position: inside; }
clear
python3 app.py
npm install -g firebase-tools
firebase login --no-localhost
4/0AXEQxIB8PJ7Gd7LMuvDnd55fcC_0xQPKAqLcB9M95TrkLqgdJU0aXyKPzZcE6yFbyrK9-A
firebase login --no-localhost
firebase init hosting
git init
git add .
git commit -m "Social 18 Flask app initial code"
python3 app.py
pip freeze > requirements.txt
echo "gunicorn" >> requirements.txt
git config --global user.name "Rohith Kalithkar"
git config --global user.email "rohithkalithkar8978@gmail.com"
git add .
git commit -m "Deploy to Render"
git branch -M main
https://github.com/rohithkalithkar8978-coder/social-18.git
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
git branch -M main
git remote add origin https://github.com/rohithkalithkar8978-coder/social-18.git
git push -u origin main
git remote set-url origin https://github.com/rohithkalithkar8978-coder/social-18.git
git branch -M main
git push -u origin main
git push https://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@github.com/rohithkalithkar8978-coder/social-18.git main
rm -rf .git
git init
echo ".cache/" > .gitignore
echo ".gemini/" >> .gitignore
echo "__pycache__/" >> .gitignore
git add app.py templates/ static/ requirements.txt .gitignore
git commit -m "Clean deployment push"
git branch -M main
git push https://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@github.com/rohithkalithkar8978-coder/social-18.git main --force
git add app.py
git commit --amend -m "Clean commit without token"
git push https://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@github.com/rohithkalithkar8978-coder/social-18.git main --force
sed -i '/dbus-python/d' requirements.txt
git add requirements.txt
git commit -m "Remove dbus-python from requirements"
git push https://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@github.com/rohithkalithkar8978-coder/social-18.git main
echo -e "Flask\ngunicorn" > requirements.txt
git add requirements.txt
git commit -m "Simplify requirements to Flask and gunicorn"
git push https://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@github.com/rohithkalithkar8978-coder/social-18.git main
git add app.py
git commit -m "Ensure Flask instance is named app"
git push https://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@github.com/rohithkalithkar8978-coder/social-18.git main
from flask import Flask, render_template
app = Flask(__name__)
# Define your sports data dictionary
sports_data = {
}
@app.route('/')
def home():
if __name__ == '__main__':;     app.run(debug=True)
git add app.py
git commit -m "Pass sports data to template"
git push https://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@github.com/rohithkalithkar8978-coder/social-18.git main
git add templates/index.html
git commit -m "Replace index.html with clean title pipe syntax"
git push https://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@github.com/rohithkalithkar8978-coder/social-18.git main
git add app.py templates/sport.html
git commit -m "Add detail page route for sports"
git push https://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@github.com/rohithkalithkar8978-coder/social-18.git main
