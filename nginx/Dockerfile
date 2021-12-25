FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY  ./loach.dev.conf /etc/nginx/conf.d
COPY ./options-ssl-nginx.conf /etc/letsencrypt/config/options-ssl-nginx.conf

