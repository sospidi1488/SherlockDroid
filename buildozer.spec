name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4

      - name: Install System Dependencies
        run: |
          sudo apt update
          sudo apt install -y git zip unzip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
          pip3 install --user --upgrade buildozer cython==0.29.33 virtualenv

      - name: Pre-install Android SDK/NDK
        run: |
          # Создаем структуру папок заранее, чтобы Buildozer не запутался
          mkdir -p ~/.buildozer/android/platform
          export PATH=$PATH:$HOME/.local/bin
          # Эта команда заставит его только скачать нужное, не начиная билд
          buildozer android sdk_update || true

      - name: Build with Buildozer
        run: |
          export PATH=$PATH:$HOME/.local/bin
          # Используем "интерактивный" ввод "yes", чтобы пройти все лицензии
          yes | buildozer android debug
        continue-on-error: false

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Sherlock-App
          path: bin/*.apk
          
