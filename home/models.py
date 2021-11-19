from django.db import models
from os import  path,mkdir
from django.conf import settings
from django.db.models.fields import CharField
# Create your models here.

class intermediates(models.Model):
    compound = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    case_no = models.CharField(max_length=100)
    class  Meta:
        ordering = ("product_name","compound","case_no")

class mill_dyes(models.Model):
    shade = models.CharField(max_length=100)
    C_I_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)
    Application = models.CharField(max_length=100)

class leveling_dyes(models.Model):
    shade = models.CharField(max_length=100)
    C_I_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)
    Application = models.CharField(max_length=100)
class acid_dyes_sub(models.Model):
    shade = models.CharField(max_length=100)
    C_I_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)
    Application = models.CharField(max_length=100)
    wool=models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")])
    Polyamide=models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")])
    Wood_Stain=models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")])
    Leather=models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")])
    Cotton=models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")])
    Paper=models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")])
    Alluminium_Anodize=models.CharField(max_length=5,choices=[('-',"yes"),('N',"No")])
    SILK=models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")])
    INK=models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")])

class metal_complex_dyes(models.Model):
    choice =[
        ("1_1_metal_complex_dyes","1 1 METAL COMPLEX DYES"),
        ("1_2_metal_complex_dyes","1 2 METAL COMPLEX DYES"),
        
    ]
    shade = models.CharField(max_length=100)
    C_I_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)
    Application = models.CharField(max_length=100)
    type = models.CharField(max_length=50,choices=choice)

#dyes
class  basic_dyes(models.Model):
    name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)
    compound = models.CharField(max_length=100)
    type = models.CharField(choices=[("L","LIQUID"),("P","POWDER")],max_length=10)
class direct_dyes(models.Model):
    shade = models.CharField(max_length=20)
    CI_Name = models.CharField(max_length = 100)
    case_no = models.CharField(max_length = 100)
    Application = models.CharField(max_length= 100)
    cotton = models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")],default='-')
    Paper = models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")],default='-')
    Ink = models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")],default='-')
    Silk = models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")],default='-')
    Polyamide = models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")],default='-')
    Alluminium_Anodize = models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")],default='-')
    Wool = models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")],default='-')
    Wood_Stain = models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")],default='-')
    Leather = models.CharField(max_length=5,choices=[('Y',"yes"),('-',"No")],default='-')

class blended_color(models.Model):
    product_name = models.CharField(max_length=50)
    case_no = models.CharField(max_length=100)

class FD_c_color(models.Model):
    FD_C_color = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    Hue = models.CharField(max_length=100)

class food_color(models.Model):
    product_name = models.CharField(max_length=200)
    ci_no  = models.CharField(max_length=50)
    FD_C_color = models.CharField(max_length= 100)
    CI_refrence = models.CharField(max_length=100)
    EC_no = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)

class lake_color_dyes(models.Model):
    product_name = models.CharField(max_length=200)
    ci_no  = models.CharField(max_length=100)
    EEC_no = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)


class solvet_dyes(models.Model):
    product_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)
class reactive_dyes(models.Model):
    choice =[
        ("HE_dyes","Reactice He Dyes"),
        ("Hot_dyes","Reactice Hot Dyes"),
        ("ME_dyes","Reactice Me Dyes"),
        ("printing_dyes_1","Reactice Printing  Dyes 1"),
        ("printing_dyes_2","Reactice Printing  Dyes 2"),
        ("vinyl_sulphone_base_dye","REACTIVE VINYL SULPHONE BASE DYE"),
    ]
    product_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)
    type = models.CharField(choices=choice,max_length=50)
class D_C_color(models.Model):
    CI_no = models.CharField(max_length=20)
    D_C_no = models.CharField(max_length=100)
    CI_Name = models.CharField(max_length=100)
# class lake_color(models.Model):
#     product_name = models.CharField(max_length=100)
#     color_index_no = models.CharField(max_length=50)
#     EEC_no =    models.CharField(max_length=10)
#     CASE_no = models.CharField(max_length=100)
#     Other_name = models.CharField(max_length=100)
class essential_oil(models.Model):
    oil_choices =[
        ("ant_bac","Anti Bacterial Oil"),
        ("anti_","antiviral Oil"),
        ("carrier","carrier Oil"),
        ("C_B","Clay & Butter Oil"),
        ("Frag","Fragrance Oil"),
        ("herb","Herbal Oil"),
        ("N_E","Natural Essential Oil"),
        ("N_i","Nature Identical Oils"),
        ("org_cold_press","Organic Cold Pressed Oils"),
        ("org_ess_oil","Organic Essential Oil"),
    ]
    product_name = models.CharField(max_length=100)
    oil_type = models.CharField(max_length=20,choices=oil_choices)
class oleoresin_oil(models.Model):
    product_name  = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)
    botonic_name = models.CharField(max_length = 100)

class natural_flower_oil(models.Model):
    product_name  = models.CharField(max_length=100)
    case_no = models.CharField(max_length=100)
    botonic_name = models.CharField(max_length = 100)



#panding to add in admin model to show in column also panding design
#pharma models
class veterinary_apis(models.Model):
    name_of_api = models.CharField(max_length=100)
    case_no = models.CharField(max_length=40)
    Therapeutic_Segments = models.CharField(max_length=100)


class ref_std_impurities(models.Model):
    impurity_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=50)
    Product_name  = models.CharField(max_length=100)
class pellet(models.Model):
    name_of_api = models.CharField(max_length=100)
    case_no = models.CharField(max_length=40)
    Therapeutic_Segments = models.CharField(max_length=100)
class patented_impurity(models.Model):
    impurity_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=50)
    Product_name  = models.CharField(max_length=100)

class medical_supply_equip(models.Model):
    product_name = models.CharField(max_length=200)

class poultry(models.Model):
    product_name = models.CharField(max_length=100)
    presentation = models.CharField(max_length=50)
    dosage_form = models.CharField(max_length=100)
    therapeutic_segments = models.CharField(max_length=100)

class other_products(models.Model):
    product_name = models.CharField(max_length=100)
    presentation = models.CharField(max_length=50)
    dosage_form = models.CharField(max_length=100)
    therapeutic_segments = models.CharField(max_length=100)

class  livestock_product(models.Model):
    product_name = models.CharField(max_length=100)
    presentation = models.CharField(max_length=50)
    dosage_form = models.CharField(max_length=100)
    therapeutic_segments = models.CharField(max_length=100)
class companion_animal_product(models.Model):
    product_name = models.CharField(max_length=100)
    presentation = models.CharField(max_length=50)
    dosage_form = models.CharField(max_length=100)
    therapeutic_segments = models.CharField(max_length=100)

class tablet_capsules(models.Model):
    product_name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
class combination_formulations(models.Model):
    product_name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)


class Stabilized_vitamins(models.Model):
    product_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=50)
    strength = models.CharField(max_length=100)
class Specialities(models.Model):
    product_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=50)
    strength = models.CharField(max_length=100)
class Minerals(models.Model):
    product_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=50)
    strength = models.CharField(max_length=100)
class amino_acid(models.Model):
    product_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=50)
    strength = models.CharField(max_length=100)

class oral_suspensions(models.Model):
    product_name = models.CharField(max_length=100)

class nasal_drop(models.Model):
    product_name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)

class ointments(models.Model):
    product_name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)

class injectables(models.Model):
    product_name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)




#shades & pigments Table

class shades_and_pigment(models.Model):
    choices =[
        ("waterbase_intjet_ink","Waterbase inkjet Int"),
        ("universal_stainer","Universal Stainer"),
        ("paints","paints"),
        ("machine_cotaing_colorant","Machine Cotaing Colorant"),
        ("inorganic_pigment","Inorganic Pigment"),
        ("industrial_coating","Industrial Coating"),
        ("cement_architecture_dispersion","Cement Architecture Dispersion"),
        ("architecture_paint","Architecture Paints"),
        ("13_waterbase_flexo_ink","13 Waterbase Flexo ink"),
        ("11_mixed_meta_oxides","11 Mixed Meta Oxides"),
        ("08_12_pvc_masterbatches","08 + 12 Pvc and Pvc Master Batches"),
        ("toner_fanal_pigment","Toner Fanal Pigments"),
        ("hign_performance_pigment","High Performance Pigments"),
    ]    
    product_name = models.CharField(max_length=100)
    case_no = models.CharField(max_length=15)
    type = models.CharField(max_length=50,choices=choices)

class flouroscent_pigments(models.Model):
    product_name = models.CharField(max_length=100)









    #---------------------------------------------------------------pages content classes-----------------------------------

class home_image(models.Model):
    image= models.ImageField('/home_images/')
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

class company_detail(models.Model):
    Company_name = models.CharField(max_length = 10)
    Address_Line_1 = models.CharField(max_length=100)
    Address_Line_2 = models.CharField(max_length=100)
    pincode = models.IntegerField()
    customer_care_number = models.IntegerField()
    customer_care_Email_Id = models.EmailField()
    sales_department_number=models.IntegerField(default=-1)
    sales_department_email_id=models.EmailField(default="sales@kewinchem.com")
    sales_department_email_id_pass = models.CharField(max_length=20)
    facebook_page = models.CharField(max_length = 100)
    whatsup_link = models.CharField(max_length = 100)
    we_chat_link = models.CharField(max_length=100)



class about_us(models.Model):
    history = models.TextField()
    our_vision = models.TextField()
    out_mission = models.TextField()
    our_value = models.TextField()
class news_feed_POST(models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now=True)
    description = models.TextField()
    Event_Brief = models.TextField()
class Post_images(models.Model):
    post = models.ForeignKey(news_feed_POST,on_delete=models.CASCADE)
    image_title = models.CharField(max_length=150,default="")
    image = models.ImageField(upload_to = "news_feed")
class user_query(models.Model):
    User_Name = models.CharField(max_length=100)
    User_Email = models.EmailField()
    User_mobile = models.CharField(max_length=15)
    User_Query = models.TextField()



class user_Requirement(models.Model):
    Full_name = models.CharField(max_length=200)
    email_id = models.EmailField()
    mobile_number = models.CharField(max_length=13)
    Requirement_file = models.FileField(upload_to='user_requirement/')


class category_images(models.Model):
    choices = (
        [0,"Default"],
        [1,"Dyes & Intermidiates"],
        [2,"Food & Pharma"],
        [3,"Varieties in Cosmetic"],
        [4,"Shades of  pigments"],
        [5,"Intermediates"],
        [6,"Acid Dyes"],
        [7,"Basic Dyes"],
        [8,"Direct Dyes"],
        [9,"Food & Lake Color"],
        [10,"Solvet Dyes"],
        [11,"Reactive Dyes"],
        [12,"D & C Color Main"],
        [13,"Essential Oil"],
        [14,"Lake Color"],
        [15,"Anti Bacterial Oil"],
        [16,"antiviral Oil"],
        [17,"carrier Oil"],
        [18,"Clay & Butter Oil"],
        [19,"Fragrance Oil"],
        [20,"Herbal Oil"],
        [21,"Natural Essential Oil"],
        [22,"Nature Identical Oils"],
        [23,"Organic Cold Pressed Oils"],
        [24,"Organic Essential Oils"],
        [25,"Oleoresin Oil"],
        [26,"Natural Flower Oil"],
        [27,"Veterinary Formulation"],
        [28,"Veterinary Apis"],
        [29,"Tablets & Capsules"],
        [30,"Reference standards & impurities"],
        [31,"PELLETS"],
        [32,"Patented Impurity Product"],
        [33,"Nutraceuticals"],
        [34,"Nasal Drops & Oral Suspensions"],
        [35,"Medical Supplies & Equipment"],
        [36,"Injectable & Ointments"],
        [37,"Poultry Products"],
        [38,"Other Products"],
        [39,"LiveStock Products"],
        [40,"Companion Animal Products"],
        [41,"Tablets & Capsules"],
        [42,"Combination Formulations"],
        [43,"Stabilized Vitamins"],
        [44,"Specialities"],
        [45,"Minerals"],
        [46,"Amino Acids"],
        [47,"Oral Suspension"],
        [48,"NASAL DROPS"],
        [49,"ointments"],
        [50,"Injectables"],
        [51,"Waterbase inkjet Int"],
        [52,"Universal Stainer"],
        [53,"Paints"],
        [54,"Organic Pigment"],
        [55,"Machine Cotaing Colorant"],
        [56,"Inorganic Pigment"],
        [57,"Industrial Coating"],
        [58,"Cement Architecture Dispersion"],
        [59,"Architecture Paints"],
        [60,"13 Waterbase Flexo ink"],
        [61,"11 Mixed Meta Oxides"],
        [62,"08 + 12 Pvc and Pvc Master Batches"],
        [63,"Toner Fanal Pigments"],
        [64,"High Performance Pigments"],
        [65,"Flouroscent Pigments"],
        [66,"Milling Dyes"],
        [67,"Levelling Dyes"],
        [68,"Acid Dyes"],
        [69,"1 1 METAL COMPLEX DYES"],
        [70,"1 2 METAL COMPLEX DYES"],
        [71,"Liquid"],
        [72,"Powder"],
        [73,"Blended Color"],
        [74,"D & C Color Sub-category"],
        [75,"FD & C Color"],
        [76,"Food  Color"],
        [77,"Lake Color"],
        [78,"Reactice He Dyes"],
        [79,"Reactice Hot Dyes"],
        [80,"Reactice Me Dyes"],
        [81,"Reactice Printing  Dyes 1"],
        [82,"Reactice Printing  Dyes 2"],
        [83,"REACTIVE VINYL SULPHONE BASE DYE"],
        )
    category_type = models.IntegerField(choices=choices,default=0)
    Refrence_image = models.ImageField(upload_to="category/media/",default="category/media/default.jpg")
    def __str__(self):
        return str(self.category_type)