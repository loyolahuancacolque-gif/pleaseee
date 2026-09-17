[app]

title = Dino Runner 2 Ultimate
package.name = dinorunner2
package.domain = org.dino.runner

source.dir = .
source.include_exts = py,png,jpg,jpeg,wav,ogg,mp3,ttf,json,txt

version = 2.0

# numpy es opcional en main.py; se omite para evitar fallos de compilacion.
requirements = python3,pygame

orientation = landscape
fullscreen = 1

android.presplash_color = #0A1428
android.archs = arm64-v8a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

# Si agregas icono/presplash propios, descomenta:
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
