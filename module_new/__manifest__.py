# -*- coding: utf-8 -*-
##############################################################################
#
#    SLTECH ERP SOLUTION
#    Copyright (C) 2023-Today(www.slecherpsolution.com).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "School",
    "category": "Purchase/Sale",
    "author": "Ritwik sadhu",
    "website": "https://www.sltecherpsolution.com/",
    "depends": [
        "base"
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/students.xml',
        'views/classes.xml',
        'views/teachers.xml',
        'views/subjects.xml',
        'views/school.xml',
    ],

    "installable": True,
    "auto_install": False,
    "application": False,
    "price": 0.0,
    "currency": "EUR",
    "license": "AGPL-3",
    "development_status": "Sachin Burnawal",
    "maintainers": ["Sachin Burnawal"],
}

