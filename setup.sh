sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4
sudo apt-get install libqt4-test
sudo apt-get install python3-pyqt5

sudo apt-get install wget build-essential checkinstall -y&& \
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev -y && \
wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz && \
tar xzf Python-3.7.9.tgz && \
cd Python-3.7.9 && \
./configure --enable-optimizations && \
sudo make altinstall

sudo apt-get install python3-venv

cd ~/
mkdir env
python3 -m venv ~/env/PiEnv
source ~/env/PiEnv/bin/activate