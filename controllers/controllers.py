# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class SceTicket(http.Controller):
    @http.route('/sce_ticket/index', auth="public", website=True)
    def ticket_index(self, search='', **post):
        key = ""
        ticket_list = []
        domain = [('state', '=', 'published'),]
        user = request.env.user
        Ticket = request.env['sce_ticket.ticket']
        tickets = Ticket.search(domain)
        # print("-------------- request.env ----------------")
        # print(request.env)
        topped1 = ''
        topped2 = ''
        if post.get('topped'):
            # print('-------------- enter topped --------------')
            ticket_num = post['topped'].strip()
            ticket = Ticket.search([('id','=',ticket_num)])
            user = request.env.user
            topped1 = Ticket.top(user,ticket)
            if topped1:
                if topped1.ticket_id.id:
                    ticket_list.append(
                        {
                            'id': topped1.ticket_id.id,
                            'name': topped1.ticket_id.name,
                            'address': topped1.ticket_id.address,
                            'phone': topped1.ticket_id.phone,
                            'bank_name': topped1.ticket_id.bank_name,
                            'bank_number': topped1.ticket_id.bank_number,
                            'duty_number':topped1.ticket_id.duty_number,
                            'topped':'on'
                        }
                    )
            # print('-------------- ticket.top --------------')
        if topped1:
            topped2 = request.env['sce_ticket.top'].search([('topper', '=', user.id),('ticket_id','!=',topped1.ticket_id.id)])
            for topped in topped2:
                if topped.ticket_id.id:
                    ticket_list.append(
                        {
                            'id': topped.ticket_id.id,
                            'name': topped.ticket_id.name,
                            'address': topped.ticket_id.address,
                            'phone': topped.ticket_id.phone,
                            'bank_name': topped.ticket_id.bank_name,
                            'bank_number': topped.ticket_id.bank_number,
                            'duty_number': topped.ticket_id.duty_number,
                            'topped': 'on'
                        }
                    )
        else:
            topped2 = request.env['sce_ticket.top'].search([('topper', '=', user.id)])
            for topped in topped2:
                if topped.ticket_id.id:
                    ticket_list.append(
                        {
                            'id':topped.ticket_id.id,
                            'name': topped.ticket_id.name,
                            'address': topped.ticket_id.address,
                            'phone': topped.ticket_id.phone,
                            'bank_name': topped.ticket_id.bank_name,
                            'bank_number': topped.ticket_id.bank_number,
                            'duty_number': topped.ticket_id.duty_number,
                            'topped': 'on'
                        }
                    )
        if ticket_list:
            ids = []
            for ticket in ticket_list:
                print(ticket['id'])
                ids.append(ticket['id'])
            domain.append(('id','not in',ids))
            tickets = Ticket.search(domain)
            for ticket in tickets:
                if ticket.id:
                    ticket_list.append(
                        {
                            'id': ticket.id,
                            'name': ticket.name,
                            'address': ticket.address,
                            'phone': ticket.phone,
                            'bank_name': ticket.bank_name,
                            'bank_number': ticket.bank_number,
                            'duty_number': ticket.duty_number,
                            'topped': 'off'
                        }
                    )
        else:
            for ticket in tickets:
                if ticket.id:
                    ticket_list.append(
                        {
                            'id': ticket.id,
                            'name': ticket.name,
                            'address': ticket.address,
                            'phone': ticket.phone,
                            'bank_name': ticket.bank_name,
                            'bank_number': ticket.bank_number,
                            'duty_number': ticket.duty_number,
                            'topped': 'off'
                        }
                    )
        if post.get('search_box'):
            # print('-------------- enter search_box --------------')
            if post['search_box']:
                key = post['search_box'].strip()
                # domain.append(('name','ilike',key))
                # tickets = Ticket.search(domain)
                if key:
                    ticket_list2 = []
                    # print(key)
                    for ticket in ticket_list:
                        if key in ticket['name']:
                            print(ticket['name'])
                            ticket_list2.append(ticket)
                    # print(ticket_list2)
                    ticket_list = ticket_list2
                    # print(ticket_list)
        values = {
            "tickets":tickets,
            'search': key,
            "ticket_list":ticket_list,
        }
        return http.request.render('sce_ticket.ticket', values)

    @http.route('/sce_ticket/ticket/detail/<model("sce_ticket.ticket"):ticket>', auth="public", website=True)
    def ticket_detail(self, ticket, **kw):
        # print('ok')
        # print(ticket)
        return http.request.render('sce_ticket.detail',{
            'ticket': ticket,
            })

    # @http.route('/sce_ticket/ticket/top/<model("sce_ticket.ticket"):ticket>', auth="public", website=True)
    # def topped(self, ticket, **post):
    #     user = request.env.user
    #     print(user)
    #     print('enter toppedd')
    #     print(ticket)
    #     print(ticket.id)
    #     ticket_id = post['topped'].strip()

    #     # top = request.env['sce_ticket.top'
    #     Top = request.env['sce_ticket.top']
    #     tops = Top.search([('topper','=',user.id)])
    #     print(tops)
    #     print("=========")
    #     for top in tops:
    #         print(top.id)
    #         print(top.topper)
    #         print(top.ticket_id)
    #         print(top.ticket_id.name)
    #         print(top.is_on)
    #     print("=========")
    #     Ticket = request.env['sce_ticket.ticket']
    #     ticket = Ticket.search([('id', '=', ticket_id), ])
    #     ticket.top(user, ticket_id)
    #     print(ticket)
    #     print(ticket.name)

    #     return http.request.render('sce_ticket.ticket', {
    #         'tickets': ticket,
    #         "topped": 'on',
    #     })