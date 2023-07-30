FROM odoo:16.0

USER root

COPY ./compose/odoo/etc/odoo.conf /etc/odoo/odoo.conf
COPY ./compose/odoo/etc/requirements.txt /etc/odoo/requirements.txt

RUN chown odoo:odoo /etc/odoo

# Added to allow debugging on VSCode
RUN pip install -U debugpy
RUN pip install -U ptvsd
RUN pip install -r /etc/odoo/requirements.txt

USER odoo
