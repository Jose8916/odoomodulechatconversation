from odoo import api, models, fields

class ModalConversacionWizard(models.TransientModel):
    _name = "modal.conversacion.wizard"

    total_fees = fields.Float(string="Fees")

    def observar_modal_conversacion(self):
        print("modal abierto")
        return True