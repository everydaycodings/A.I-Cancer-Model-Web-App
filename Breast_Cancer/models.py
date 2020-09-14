from django.db import models

# Create your models here.
OPTION = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10)
)

RESULT = (
    (0, "Cancer"),
    (1, "Non-Cancer")
)

class Data(models.Model):
    clump_thickness = models.IntegerField("Clump Thickness", choices=OPTION)
    cell_size = models.IntegerField("Cell Size", choices=OPTION)
    cell_shape = models.IntegerField("Cell Shape", choices=OPTION)
    marginal_adhesion = models.IntegerField("Marginal Adhesion", choices=OPTION)
    s_e_s_c = models.IntegerField("S.E.S.C", choices=OPTION)
    bare_nuclei = models.IntegerField("Bare Nuclei", choices=OPTION)
    bland_chromatin = models.IntegerField("Bland Chromatin", choices=OPTION)
    normal_nucleoli = models.IntegerField("Normal Nucleoli", choices=OPTION)
    mitoses = models.IntegerField("Mitoses", choices=OPTION)
    result = models.IntegerField("Result", choices=RESULT, default=1)

    def __str__(self):
        return str(self.clump_thickness)