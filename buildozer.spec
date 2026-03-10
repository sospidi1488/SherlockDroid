[app]
title = Sherlock Droid
package.name = sherlock_osint
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Добавил библиотеку requests, она нужна для работы Sherlock
requirements = python3,kivy,requests,urllib3,charset-normalizer,idna

orientation = portrait
fullscreen = 0

# Настройки сборки
android.archs = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
