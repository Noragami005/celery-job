to start celery job 
configure settings before start !! 

--cd basic_celery_job X 2 
--celery -A celery worker               

It is usally advise against directly embedding the Nginx configuration
within your Django project files for several reasons,
but it is just for this one case. 
You don't need to change directory.


once complete just run 
-- sudo systemctl reload nginx
