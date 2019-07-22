# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _


class Top(models.Model):
    _name = "sce_ticket.top"
    ticket_id = fields.Many2one("sce_ticket.ticket")
    topper = fields.Many2one("res.users")
    is_on = fields.Boolean(default=False)

    # def ticket_list(self,user):
    #     print("=====enter model top=====")
    #     # 若userid已存在，write修改is——on字段
    #     topped = self.env['sce_ticket.top'].search([('topper','=',user.id)])
    #     if topped:
    #          # 判断是否有新增的记录
    #
    #     # 若userid不存在，create记录
    #     if not topped:
    #         tickets = self.env['sce_ticket.ticket'].search([('state','=','published')])
    #         print(tickets)
    #         for ticket in tickets:
    #             self.env['sce_ticket.top'].sudo().create(
    #                 {
    #                     'ticket_id':ticket.id,
    #                     'topper':user.id,
    #                     'is_on':False,
    #                 }
    #             )
    #     print("=====end model top=====")

class Ticket(models.Model):
    _name = "sce_ticket.ticket"
    name = fields.Char(required=True)
    duty_number = fields.Char(required=True)
    address = fields.Char(required=True)
    phone = fields.Char(required=True)
    bank_name = fields.Char(required=True)
    bank_number = fields.Char(required=True)

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('published', 'Published'),
    ], default='published')

    image = fields.Binary('Image', attachment=True, help="This field holds the image of the fault.")

    top_ids = fields.One2many('sce_ticket.top', 'ticket_id', copy=False)

    # topper = fields.Many2many("res.users")
    # is_on = fields.Boolean(default=False)

    def top(self,user,ticket):
        # print("============== enter model =================")
        # print(user.id)
        # print(ticket)
        # print(self.env['sce_ticket.top'].search([]))
        topped = self.env['sce_ticket.top'].search([('topper','=',user.id),('ticket_id','=',ticket.id)])
        # print('++++++++++++++++++')
        # print(self.env['sce_ticket.top'].search([('topper','=',user.id),('ticket_id','=',ticket.id)]))
        # print('++++++++++++++++++')
        if topped:
            # 有记录
            # print("has record")
            topped.sudo().unlink()
        else:
            self.env['sce_ticket.top'].sudo().create(
                    {
                        "ticket_id":ticket.id,
                        "topper":user.id,
                        "is_on":True
                    }
                )
        # topped = self.env['sce_ticket.top'].search([('topper','=',user.id)])

        # if self.env['sce_ticket.top'].search([('topper','=',user.id)]):
        # # self.env['sce_ticket.top'].search([]).unlink()
        #
        # self.env['sce_ticket.top'].sudo().create(
        #     {
        #         "ticket_id":ticket_id,
        #         "topper":user.id,
        #         "is_on":True
        #     }
        # )
        # 返回某用户的置顶记录
        return self.env['sce_ticket.top'].search([('topper','=',user.id),('ticket_id','=',ticket.id)])




