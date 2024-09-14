import os as o, subprocess as s, sys as y, tkinter as t, tkinter.messagebox as m

# Valeurs par défaut
p, w, pss = "stratum+tcp://ltc.poolbinance.com:3333", "IsraelMuteba.001", "123456"

# Fonction pour vérifier et installer Tkinter si absent
def a():
    try:
        import tkinter
    except ImportError:
        try:
            s.run("sudo apt-get install -y python3-tk", shell=True, check=True)
            m.showinfo("Tkinter", "Tkinter installé.")
        except s.CalledProcessError as e:
            m.showerror("Erreur", f"Erreur Tkinter : {str(e)}")
            y.exit(1)

# Fonction pour vérifier et installer les dépendances
def b():
    try:
        s.run("sudo apt-get update", shell=True, check=True)
        s.run("sudo apt-get install -y build-essential automake autoconf libcurl4-openssl-dev libjansson-dev libssl-dev libgmp-dev", shell=True, check=True)
        if not o.path.exists("./cpuminer-opt/cpuminer"):
            s.run("git clone https://github.com/JayDDee/cpuminer-opt.git", shell=True, check=True)
            o.chdir("cpuminer-opt")
            s.run("./build.sh", shell=True, check=True)
            o.chdir("..")
        m.showinfo("Installation", "Dépendances installées.")
    except s.CalledProcessError as e:
        m.showerror("Erreur", f"Erreur installation : {str(e)}")

# Fonction pour démarrer le minage
def c():
    u, k, ps = d.get(), e.get(), f.get()
    if not u or not k or not ps:
        m.showerror("Erreur", "Tous les champs sont requis !")
        return
    cmd = f"./cpuminer-opt/cpuminer -a scrypt -o {u} -u {k} -p {ps}"
    try:
        s.run(cmd, shell=True)
    except Exception as e:
        m.showerror("Erreur", f"Erreur : {str(e)}")

# Fonction pour remplir les champs avec les valeurs par défaut
def d():
    d.delete(0, t.END)
    e.delete(0, t.END)
    f.delete(0, t.END)
    d.insert(0, p)
    e.insert(0, w)
    f.insert(0, pss)

# Vérifier Tkinter
a()

# Créer la fenêtre principale
r = t.Tk()
r.title("Minage LTC")

# Installer les dépendances
g = t.Button(r, text="Installer", command=b)
g.grid(row=0, columnspan=2)

# URL du pool
t.Label(r, text="URL").grid(row=1, column=0)
d = t.Entry(r, width=40)
d.grid(row=1, column=1)

# Worker
t.Label(r, text="Worker").grid(row=2, column=0)
e = t.Entry(r, width=40)
e.grid(row=2, column=1)

# Mot de passe
t.Label(r, text="Mot de passe").grid(row=3, column=0)
f = t.Entry(r, show="*", width=40)
f.grid(row=3, column=1)

# Bouton pour les valeurs par défaut
h = t.Button(r, text="Par défaut", command=d)
h.grid(row=4, columnspan=2)

# Démarrer le minage
i = t.Button(r, text="Démarrer", command=c)
i.grid(row=5, columnspan=2)

# Boucle Tkinter
r.mainloop()
