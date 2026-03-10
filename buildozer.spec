[app]
title = Sherlock Droid
package.name = sherlock_osint
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# В требования добавил requests, так как Sherlock работает через сеть
requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

# Критически важные настройки для Android
android.archs = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1 
