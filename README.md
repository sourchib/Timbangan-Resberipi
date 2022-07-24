# backup timbangaan
Komponen Software
<ul>
<li>Aplikasi imager</li>
<li>Iso Resberipi</li>
<li>Python version 3</li>
<li>pip & pip3</li>
</ul>

Komponen Hardware
<ul>
<li>Resberipi 3</li>
<li>USB to Serial</li>
<li>Card Reader</li>
<li>Memory Card</li>
</ul>

Instalasi ISO Resberipi
<ul>
<li>Running aplikasi Imager Resberipi download di folder iso imager</li>
<li>Colokan adaptor resberipi</li>
<li>Copot memory card dan tancapkan ke laptop</li>
<li>Copy file program wpa_supplicant.conf ke dalam file boot pada card memery</li>
<li>kemudian masukkan kembali card ke resberipi</li>
<li>Nyalakan Resberipi 3</li>
<li>Tunggu sampai boot selesai</li>
<li>Cek ipaddress dengan perintahn ipconfig di terminal</li>
<li>Buka aplikasi ipscanner atau nmap pada laptop</li>
<li>Cari nama device Resberipi</li>
<li>Buka SSH masuukan hostname ipaddress dan port ssh 22</li>
<li>Login username dan password resberipi OS</li>
</ul>

Instalasi Software
<ul>
<li>Buka terminal OS Resberipi</li>
<li>raspi-config konfigurasi wifi</li>
<li>ping 8.8.8.8</li>
<li>konfigurasi WiFi
<a href ="https://weworkweplay.com/play automatically-connect-a-raspberry-pi-to-a-wifi-network">Button link </a></li>
<li>apt-get update</li>
<li>apt-get upgrade</li>
<li>hostname && hostname -f samakan</li>
<li>dpkg-reconfigure locales</li>
<li>pilih lokasi ID</li>
<li>locale-gen</li>
<li>apt-get install ntp</li>
<li>nano /etc/ntp.conf</li>
<li>ketik control + w kemudian control + r cari nama debian enter kemudian ganti dengan id All</li>
<li>ntpq -p jika nilai 0 maka berhasil</li>
<li>raspi-config konfigurasi jam</li>
<li>date cek jam sesuai</li>
<li>nano /etc/bash.bacrc</li>
<li>python --version</li>
<li>install pip untk kebutuhn library python..</li>
<li>download file timbangan.py</li>
<li>cek serial monitor dengan perintah :  ln -l /dev/ttyUSB0 </li>
<li>nano timbangan.py ganti port seial sesuai /dev/tty?</li>
<li>jalankan program dengan python3 timbangan.py</li>
<li>Jika ada library yang belum terinstall gunakan perintah pip nama library</li>
<li>Gunakan schedule dengan cronjob</li>
</ul>

Instalasi Ngrok atau OPENVPN untuk remote :
<ul>
<li>Konfiurasi Ngrok RSPI<a href="https://medium.com/@gaelollivier/connect-to-your-raspberry-pi-from-anywhere-using-ngrok-801e9fd1dd46">
Link
</a></li>
</ul>

Program reboot otomatis ketika tidak ada Koneksi Internet : 
<ul>
<li>cd /home/folder</li>
<li>nano cek_internet.sh</li>
<li>tambahkan perintah ini</li>
<p>
#!/bin/bash

TMP_FILE=/tmp/inet_up
no_inet_action() {
    shutdown -r +1 'No internet.'
}
if ping -c5 google.com; then
    echo 1 > $TMP_FILE
else
    [[ `cat $TMP_FILE` == 0 ]] && no_inet_action || echo 0 > $TMP_FILE
fi
</p>
<li>chmod +x cek_internet.sh</li>
</ul>

Cronjob Schedule Program Python
<ul>
<li>Gunakan bantuan https://crontab.guru/</li>
<li>apt-get install cron</li>
<li>/etc/init.d/crontab status</li>
<li>nano /etc/crontab</li>
<li>tambahkan perintah seperti dibawah ini :</li>
<p>* * * * * root /usr/bin/python3 /home/kandang/timbang/timbangan.py</p>
<p>* * * * * root /usr/bin/ngrok tcp 22</p>
<p>30 * * * * root /home/folder/cek_internet.sh</p>
</ul>