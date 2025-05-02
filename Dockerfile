# Base image
FROM nginx:alpine

# Copy your HTML and CSS files into the nginx web directory
COPY index.html /usr/share/nginx/html/index.html
COPY style.css /usr/share/nginx/html/style.css

# Expose default Nginx port
EXPOSE 80

# No CMD needed; nginx image already handles it

