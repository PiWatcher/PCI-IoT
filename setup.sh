sudo apt-get install libatlas-base-dev -y
sudo apt-get install libjasper-dev -y
sudo apt-get install libqtgui4 -y
sudo apt-get install libqt4-test -y
sudo apt-get install python3-pyqt5 -y
sudo apt-get install python3-h5py

cd ~/

sudo apt-get install wget build-essential checkinstall -y&& \
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev -y && \
wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz && \
tar xzf Python-3.7.9.tgz && \
cd Python-3.7.9 && \
./configure --enable-optimizations && \
sudo make altinstall

sudo rm -rf Python-3.7.9
sudo rm -rf Python-3.7.9.tgz

sudo apt-get install python3-venv -y

cd ~/
mkdir env
python3.7 -m venv ~/env/PiEnv
source ~/env/PiEnv/bin/activate

python -m pip install --upgrade pip
