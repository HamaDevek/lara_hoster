import os
import random
import subprocess



def install_nginx():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install nginx -y')
    print('nginx installed successfully!')
def install_mysql():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install mysql-server -y')
    os.system('sudo systemctl start mysql.service')
    os.system('sudo mysql_secure_installation')
    os.system('sudo systemctl start mysql.service')
    print('[!] Mysql installed successfully!')

def install_laravel():
    version = input('[+] please type php version for example 8.1 >> ')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install software-properties-common -y')
    os.system('sudo add-apt-repository ppa:ondrej/php -y')
    if version =='8.1':
        os.system('sudo apt-get install php8.1 php8.1-mbstring php8.1-gettext php8.1-zip php8.1-fpm php8.1-curl php8.1-mysql php8.1-gd php8.1-cgi php8.1-soap php8.1-sqlite3 php8.1-xml php8.1-redis php8.1-bcmath php8.1-imagick php8.1-intl -y')  
    else:
        os.system('sudo apt-get install php'+version+' php'+version+'-mbstring php'+version+'-gettext php'+version+'-zip php'+version+'-fpm php'+version+'-curl php'+version+'-mysql php'+version+'-gd php'+version+'-cgi php'+version+'-soap php'+version+'-sqlite3 php'+version+'-xml php'+version+'-redis php'+version+'-bcmath php'+version+'-imagick php'+version+'-intl -y')
    os.system('sudo sudo apt-get install git composer -y')
    print(' composer and php installed successfully!')
def add_new_domain(domain):
    

    os.system('sudo mkdir /var/www/html/'+str(domain))
    os.system('sudo chown -R www-data:www-data /var/www/html/'+str(domain))
    confx ='''

    server {
        listen 80;
        server_name '''+domain+''';
        root /var/www/html/'''+domain+'''/public;

        add_header X-Frame-Options "SAMEORIGIN";
        add_header X-Content-Type-Options "nosniff";

        index index.php;

        charset utf-8;

        location / {
            try_files $uri $uri/ /index.php?$query_string;
        }

        location = /favicon.ico { access_log off; log_not_found off; }
        location = /robots.txt  { access_log off; log_not_found off; }

        error_page 404 /index.php;

        location ~ \.php$ {
            fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
            fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
            include fastcgi_params;
        }

        location ~ /\.(?!well-known).* {
            deny all;
        }
    }
    '''


    f=open('/etc/nginx/sites-available/'+domain+'.conf','w')
    f.write(confx)
    f.close()
    os.system('sudo ln -s /etc/nginx/sites-available/'+domain+'.conf /etc/nginx/sites-enabled/'+domain+'.conf')
    os.system('sudo systemctl restart nginx')

    print('[!] every thing done but if you got any problem with permsion run this command')
    print('[!] chown -R www-data:www-data /var/www/html/'+domain)



def remove_domain(domain):
    
    os.system('sudo rm -r /var/www/html/'+str(domain))
    os.system('sudo rm /etc/nginx/sites-available/'+domain+'.conf')
    os.system('sudo rm /etc/nginx/sites-enabled/'+domain+'.conf')
    os.system('sudo systemctl restart nginx')
    print('[!] now the '+domain+' is deleted !')


os.system('clear')

def guide_msg():

    print('''

  
░█─── ─█▀▀█ ░█▀▀█ ─█▀▀█ 　 ░█─░█ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ 
░█─── ░█▄▄█ ░█▄▄▀ ░█▄▄█ 　 ░█▀▀█ █──█ ▀▀█ ──█── █▀▀ █▄▄▀ 
░█▄▄█ ░█─░█ ░█─░█ ░█─░█ 　 ░█─░█ ▀▀▀▀ ▀▀▀ ──▀── ▀▀▀ ▀─▀▀

automaicaly host your laravel website !

from FD

github.com/FDX100
====================================''')

    print('''
1 => add new domain
2 => remove domain
3 => install nginx
4 => install mysql 
5 => install PHP & composer
other key to exit
    ''')
    try:
            
        choice = input('[!] your choice >> ')
        if (choice == '1'):
            domain = input('[!] type new domain >> ')
            add_new_domain(domain)
        elif(choice == '2'):
            domain = input('[+] type domain to remove >>')
            ch = input ('[!] are you sure you want to (y) or (n) delete '+domain+' >>')
            if (ch =='y' or ch =='Y'):
                remove_domain(domain)
            else:
                print('exit !')
        elif(choice =='3'):
            install_nginx()
        elif(choice =='4'):
            install_mysql()
        elif(choice =='5'):
            install_laravel()
        else:
            print('[!] scipt is exited ')
            exit()    
    except KeyboardInterrupt:
        print('[!] Lara Hoster is exited')
root_command=subprocess.check_output(['whoami'])

if('root' in str(root_command)):
    
    while True:
        


        guide_msg()

else:
    print('[!] please run this tool as root')
