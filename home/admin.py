from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(intermediates)
class intermediatesAdmin(admin.ModelAdmin):
    list_display = ("compound","product_name","case_no")
    list_filter = ("compound","product_name","case_no")
    list_per_page = 20

@admin.register(D_C_color)
class D_C_colorAdmin(admin.ModelAdmin):
    list_display = ("CI_no","D_C_no","CI_Name")
    list_filter = ("D_C_no","CI_Name")
    search_fields = ("CI_no","D_C_no","CI_Name")
    list_per_page = 20

@admin.register(mill_dyes)
class mill_dyesAdmin(admin.ModelAdmin):
    list_display = ("shade", "C_I_name", "case_no", "Application")
    list_filter = ("shade", "C_I_name", "Application")
    search_fields = ("shade", "C_I_name", "case_no", "Application")

@admin.register(leveling_dyes)
class leveling_dyesAdmin(admin.ModelAdmin):
    list_display = ("shade", "C_I_name", "case_no", "Application")
    list_filter = ("shade", "C_I_name", "Application")
    search_fields = ("shade", "C_I_name", "case_no", "Application")

@admin.register(acid_dyes_sub)
class acid_dyes_subAdmin(admin.ModelAdmin):
    list_display = ("shade", "C_I_name", "case_no", "Application","wool", "Polyamide", "Wood_Stain", "Leather", "Cotton", "Paper", "Alluminium_Anodize", "SILK", "INK")
    list_filter = ("shade", "C_I_name", "Application","wool", "Polyamide", "Wood_Stain", "Leather", "Cotton", "Paper", "Alluminium_Anodize", "SILK", "INK")
    search_fields = ("shade", "C_I_name", "case_no", "Application")
    

@admin.register(metal_complex_dyes)
class metal_complex_dyesAdmin(admin.ModelAdmin):
    list_display = ("shade", "C_I_name", "case_no", "Application","type")
    list_filter = ("shade", "C_I_name", "Application","type")
    search_fields = ("shade", "C_I_name", "case_no", "Application","type")


@admin.register(basic_dyes)
class basic_dyesAdminModel(admin.ModelAdmin):
    list_display = ("name","case_no","compound")
    list_filter = ("name","compound")
    search_fields = ("name","case_no","compound")
    list_per_page = 20

@admin.register(direct_dyes)
class direct_dyesAdmin(admin.ModelAdmin):
    list_display = ("shade","CI_Name","case_no","Application","cotton","Paper","Ink","Silk","Polyamide","Alluminium_Anodize","Wool","Wood_Stain","Leather")
    list_ = ("shade","CI_Name","Application","cotton","Paper","Ink","Silk","Polyamide","Alluminium_Anodize","Wool","Wood_Stain","Leather")
    list_display = ("shade","CI_Name","case_no","Application",)
    list_per_page = 20
@admin.register(blended_color)
class blended_colorAdmin(admin.ModelAdmin):
    list_display = ("product_name", "case_no")
    list_display = ("product_name",)
    list_display = ("product_name", "case_no")

@admin.register(FD_c_color)
class FD_c_colorAdmin(admin.ModelAdmin):
    list_display = ("FD_C_color","common_name", "Hue")
    list_filter = ("FD_C_color","common_name", "Hue")
    search_fields = ("FD_C_color","common_name", "Hue")

@admin.register(food_color)
class food_colorAdmin(admin.ModelAdmin):
    list_display = ("product_name" , "ci_no" , "FD_C_color", "CI_refrence", "EC_no", "case_no")
    list_filter = ("product_name" , "ci_no" , "FD_C_color", "CI_refrence", "EC_no", "case_no")
    search_fields = ("product_name" , "ci_no" , "FD_C_color", "CI_refrence", "EC_no", "case_no")
    
@admin.register(lake_color_dyes)
class lake_color_dyesAdmin(admin.ModelAdmin):
    list_display = ("product_name" , "ci_no" ,  "EEC_no", "case_no","other_name")
    list_filter = ("product_name" , "ci_no" ,"EEC_no" , "case_no","other_name")
    search_fields = ("product_name" , "ci_no" , "EEC_no", "case_no","other_name")

@admin.register(solvet_dyes)
class solvet_dyesAdmin(admin.ModelAdmin):
    list_display = ("product_name","case_no")
    list_filter = ("product_name",)
    search_fields = ("product_name","case_no")
    list_per_page = 20

@admin.register(reactive_dyes)
class reactive_dyesAdmin(admin.ModelAdmin):
    list_display = ("product_name","case_no")
    list_filter = ("product_name",)
    search_fields = ("product_name","case_no")
    list_per_page = 20


@admin.register(essential_oil)
class essential_oilAdmin(admin.ModelAdmin):
    list_display = ("product_name","oil_type")
    list_filter = ("oil_type","product_name")
    search_fields = ("product_name","oil_type")
    list_per_page = 20

# @admin.register(lake_color)
# class lake_colorAdmin(admin.ModelAdmin):
#     list_display = ("product_name", "color_index_no", "EEC_no", "CASE_no", "Other_name")
#     list_filter = ("product_name", "color_index_no", "Other_name")
#     search_fields = ("product_name", "color_index_no", "EEC_no", "CASE_no", "Other_name")
#     list_per_page = 20

@admin.register(oleoresin_oil)
class oleoresin_oilAdmin(admin.ModelAdmin):
    list_display = ("product_name", "case_no", "botonic_name")
    list_filter = ("product_name", "botonic_name")
    search_fields = ("product_name", "case_no", "botonic_name")
    list_per_page = 20

@admin.register(natural_flower_oil)
class natural_flower_oilAdmin(admin.ModelAdmin):
    list_display = ("product_name", "case_no", "botonic_name")
    list_filter = ("product_name", "case_no", "botonic_name")
    search_fields = ("product_name", "case_no", "botonic_name")
    list_per_page = 20


@admin.register(news_feed_POST)
class news_feed_POSTAdmin(admin.ModelAdmin):
    list_display = ("title", "date_time", "description", "Event_Brief")
    list_filter = ("date_time",)
    search_fields = ("title", "date_time", "description", "Event_Brief")
    list_per_page = 20

@admin.register(Post_images)
class Post_imagesAdmin(admin.ModelAdmin):
    list_display = ("post", "image_title", "image")
    list_filter = ("post", "image_title")
    search_fields = ("post", "image_title", "image")
    list_per_page = 20
@admin.register(user_query)
class user_queryAdmin(admin.ModelAdmin):
    list_display = ("User_Name", "User_Email", "User_mobile", "User_Query")
    list_filter = ("User_Name", "User_Query")
    search_fields = ("User_Name", "User_Email", "User_mobile", "User_Query")
    list_per_page = 20


@admin.register(veterinary_apis)
class veterinary_apisAdmin(admin.ModelAdmin):
    list_display = ("name_of_api","case_no","Therapeutic_Segments") 
    list_filter = ("name_of_api","Therapeutic_Segments") 
    search_fields = ("name_of_api","case_no","Therapeutic_Segments")
    list_per_page = 20
@admin.register(ref_std_impurities)
class ref_std_impuritiesAdmin(admin.ModelAdmin):
    list_display = ("Product_name","impurity_name","case_no")
    list_filter = ("Product_name","impurity_name")
    search_fields = ("Product_name","impurity_name","case_no")
    list_per_page = 20

@admin.register(pellet)
class pelletAdmin(admin.ModelAdmin):
    list_display = ("name_of_api","case_no","Therapeutic_Segments")
    list_filter = ("name_of_api","Therapeutic_Segments")
    search_fields = ("name_of_api","case_no","Therapeutic_Segments")
    list_per_page = 20

@admin.register(patented_impurity)
class patented_impurityAdmin(admin.ModelAdmin):
    list_display = ("impurity_name","case_no","Product_name")
    list_filter = ("impurity_name","Product_name")
    search_fields = ("impurity_name","case_no","Product_name")
    list_per_page = 20

@admin.register(medical_supply_equip)
class medical_supply_equipAdmin(admin.ModelAdmin):
    list_display = ("product_name",)
    list_filter = ("product_name",)
    search_fields = ("product_name",)
    list_per_page = 20

@admin.register(poultry)
class poultryAdmin(admin.ModelAdmin):
    list_display = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    list_filter = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    search_fields = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    list_per_page = 20


@admin.register(other_products)
class other_productsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    list_filter = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    search_fields = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    list_per_page = 20

@admin.register(livestock_product)
class livestock_productAdmin(admin.ModelAdmin):
    list_display = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    list_filter = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    search_fields = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    list_per_page = 20


@admin.register(companion_animal_product)
class companion_animal_productAdmin(admin.ModelAdmin):
    list_display = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    list_filter = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    search_fields = ("product_name", "presentation", "dosage_form", "therapeutic_segments")
    list_per_page = 20

@admin.register(tablet_capsules)
class tablet_capsulesAdmin(admin.ModelAdmin):
    list_display = ("product_name", "strength")
    list_filter = ("product_name", "strength")
    search_fields = ("product_name", "strength")
    list_per_page = 20

@admin.register(combination_formulations)
class combination_formulationsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "strength")
    list_filter = ("product_name", "strength")
    search_fields = ("product_name", "strength")
    list_per_page = 20

@admin.register(Stabilized_vitamins)
class Stabilized_vitaminsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "case_no", "strength")
    list_filter = ("product_name", "strength")
    search_fields = ("product_name", "case_no", "strength")
    list_per_page = 20

@admin.register(Specialities)
class SpecialitiesAdmin(admin.ModelAdmin):
    list_display = ("product_name", "case_no", "strength")
    list_filter = ("product_name", "strength")
    search_fields = ("product_name", "case_no", "strength")
    list_per_page = 20


@admin.register(Minerals)
class MineralsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "case_no", "strength")
    list_filter = ("product_name", "strength")
    search_fields = ("product_name", "case_no", "strength")
    list_per_page = 20


@admin.register(amino_acid)
class amino_acidAdmin(admin.ModelAdmin):
    list_display = ("product_name", "case_no", "strength")
    list_filter = ("product_name", "strength")
    search_fields = ("product_name", "case_no", "strength")
    list_per_page = 20


@admin.register(oral_suspensions)
class oral_suspensionsAdmin(admin.ModelAdmin):
    list_display = ("product_name",)
    list_filter = ("product_name",)
    search_fields = ("product_name",)
    list_per_page = 20


@admin.register(nasal_drop)
class nasal_dropAdmin(admin.ModelAdmin):
    list_display = ("product_name", "strength")
    list_filter = ("product_name", "strength")
    search_fields = ("product_name", "strength")
    list_per_page = 20


@admin.register(ointments)
class ointmentsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "strength")
    list_filter = ("product_name", "strength")
    search_fields = ("product_name", "strength")
    list_per_page = 20


@admin.register(injectables)
class injectablesAdmin(admin.ModelAdmin):
    list_display = ("product_name", "strength")
    list_filter = ("product_name", "strength")
    search_fields = ("product_name", "strength")
    list_per_page = 20



#shades & pigments
@admin.register(shades_and_pigment)
class shades_and_pigmentAdmin(admin.ModelAdmin):
    list_display = ("product_name","case_no", "type")
    list_filter = ("type","product_name")
    search_fields = ("product_name","case_no", "type")
    list_per_page = 20


@admin.register(flouroscent_pigments)
class flouroscent_pigmentsAdmin(admin.ModelAdmin):
    list_display = ("product_name",)
    list_filter = ("product_name",)
    search_fields = ("product_name",)
    list_per_page = 20




#-------------------------------------------pages-----------------------------------------------------------
#about us
@admin.register(about_us)
class about_usAdmin(admin.ModelAdmin):
    list_display = ("history","our_vision","out_mission","our_value")

@admin.register(home_image)
class home_imagesAdmin(admin.ModelAdmin):
    list_display = ("title","description","image")

@admin.register(company_detail)
class company_detailAdmin(admin.ModelAdmin):
    list_display = ("Company_name","Address_Line_1","Address_Line_2","pincode","customer_care_number","customer_care_Email_Id","sales_department_email_id","sales_department_email_id_pass","facebook_page","whatsup_link","we_chat_link")


@admin.register(user_Requirement)
class user_RequirementAdmin(admin.ModelAdmin):
    list_display = ("Full_name","email_id","mobile_number","Requirement_file")

@admin.register(category_images)
class category_imagesAdmin(admin.ModelAdmin):
    list_display = ("category_type","Refrence_image")