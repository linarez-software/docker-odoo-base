# Base repository for Odoo 16 on Docker

This is a base Docker Odoo project template, it contains a docker-compose.yml file.
to run this repo clone it with git:

```bash
git clone https://github.com/linarez-software/docker-odoo-base.git
```
then change to folder and run with:

```bash
sudo docker-composer up
```
then points your web browser to localhost:8069 and create a new Odoo database.

On Odoo/Applications install **Odoo module partner_loan_data for test**  module.
Grant to user(s) Manager permissions to module on Settings/Users (Loans)

## How to use this repo
### Addons
You must put all custom addons inside the folder extra-addons, this folder is mounted as a volume inside the Odoo container.

### Adding python dependencies
If your module has python dependencies you must add them to the file compose/odoo/etc/requirements.txt, this file is used by the Odoo container to install python dependencies.

That is all, happy coding!