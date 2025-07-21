# Let’s Encrypt Certificates with AWS -> on MacOS

1. 📁 Challenge-Verzeichnis auf EC2 anlegen
   ```
   sudo mkdir -p /var/www/acme/.well-known/acme-challenge
   sudo chown -R $USER /var/www/acme
   ```
2. ⚙️ NGINX-Configuration (for Challenge)

   2.1.1 install nginx:

    ```
    brew install nginx
    ```
    2.1.2 after installation you will get the path. Most proberly it will look like this: /opt/homebrew/etc/nginx/nginx.conf
  
    2.1.3 check if NGINX is working (by default its running on port 8080)
    ```
    brew services start nginx
    ```

    2.2.1 adjust confic file
    ```
    nano /opt/homebrew/etc/nginx/nginx.conf
    ```
    2.2.2 open this link in web-browser
   ```
    http://localhost:8080/.well-known/acme-challenge/test123
   ```
   2.2.3 NGINX neu starten
   ```
   brew services restart nginx
   ```
3. ⬇️ install Certbot
    ```
    brew install certbot
    ```
4. 🔐 generate Certificate (with Webroot-Method)
    ```
    mkdir -p ~/acme-challenge
    ```
    Start the certification process:
    ```
    sudo certbot certonly --webroot -w ~/acme-challenge -d example.com \
    --agree-tos --email dein@email.de --non-interactive
    ```


