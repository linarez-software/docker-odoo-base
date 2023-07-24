FROM odoo:16.0

USER odoo

COPY ./compose/odoo/etc/odoo.conf /etc/odoo/odoo.conf
COPY ./compose/odoo/etc/requirements.txt /etc/odoo/requirements.txt

RUN pip install -r /etc/odoo/requirements.txt