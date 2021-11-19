from django.core.checks import messages
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.conf import settings
from . import models as M
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from pandas import read_csv
import os
# Create your views here.


def get_ref_images(cat_type=0):
    ref_image = M.category_images.objects.filter(category_type = cat_type)
    if len(ref_image)  > 0:
        return ref_image[0]
    else:
        ref_image = M.category_images.objects.filter(category_type = 0)
        return ref_image[0]



def index(request):
    home_images = M.home_image.objects.all().reverse()
    company_details = M.company_detail.objects.first()
    return render(request, "home/home2.html",{"images":home_images,"details":company_details})


def product_home(request):
    company_details = M.company_detail.objects.first()
    
    images = []
    for i in [1,2,3,4]:
        images.append(get_ref_images(i))
    print(images)
    return render(request, "home/product_.html",{"details":company_details,"cate_images":images})


def news_feed(request):
    company_details = M.company_detail.objects.first()
    all_news_feed = M.news_feed_POST.objects.all().reverse()
    post_ = []
    for post_obj in all_news_feed:
        ref_image = M.Post_images.objects.filter(post=post_obj)
        if len(ref_image) > 0:
            ref_image = ref_image[0]
        post_.append({"post_details": post_obj, "post_ref_img": ref_image})
    return render(request, "home/news_feed.html", {"news_obj": post_,"details":company_details})


def news_post(request, post_id):
    company_details = M.company_detail.objects.first()
    post = M.news_feed_POST.objects.filter(id=post_id)
    all_images = M.Post_images.objects.filter(post=post[0])
    return render(request, 'home/news_post_full.html', {"post_details": post[0], "images_len": range(len(all_images)), "images": all_images,"details":company_details})


def about_us(request):
    company_details = M.company_detail.objects.first()
    data = M.about_us.objects.first()
    return render(request, "home/about_us.html",{"data":data,"details":company_details})


def contact_us(request):
    company_details = M.company_detail.objects.first()
    return render(request, "home/contact_us.html",{"details":company_details})


def query_form(request):
    if request.method == "POST":
        name = request.POST['name']
        mobile_number = request.POST['mobile_number']
        email_id = request.POST['email_id']
        query = request.POST['query']
        user_query_obj = M.user_query()
        user_query_obj.User_Name = name
        user_query_obj.User_Email = email_id
        user_query_obj.User_mobile = mobile_number
        user_query_obj.User_Query = query
        try:
            user_query_obj.save()
            subject = "Kewin Chemical Query Department"
            message = "Thank You For Visit.  We recieved your Query We resolve Your Query and contact to you soon"
            user_query_send(subject, message,user_query_obj.User_Email)
            subject = "Client Raise Query."
            message = "{} Raise The Query  \n Name: {} \n Mobile Number: {} \n Email Id: {} \n Query: {}".format(user_query_obj.User_Name,user_query_obj.User_Name
            ,user_query_obj.User_mobile,user_query_obj.User_Email,user_query_obj.User_Query)
            to_mail_id = M.company_detail.objects.all()[0].customer_care_Email_Id
            user_query_send(subject, message,to_mail_id)
            return JsonResponse({"ack": 0})
        except Exception as e:
            return JsonResponse({"ack": -1})
    return JsonResponse({"ack": -2})


def intermediated(request):
    company_details = M.company_detail.objects.first()
    images = []
    for i in range(5,12):
        images.append(get_ref_images(i))
    print(images)
    return render(request, "home/dye_and_.html", {"cate_name": "intermediates","details":company_details,"cate_images":images})


def Food_pharma(request):
    company_details = M.company_detail.objects.first()
    list = (
        ["veterinary_formulation",get_ref_images(27), "Veterinary Formulation"],
        ["veterinary_apis", get_ref_images(28), "Veterinary Apis"],
        ["tablets_capsules", get_ref_images(29), "Tablets & Capsules"],
        ["reference_std_impurities", get_ref_images(30), "Reference standards & impurities"],
        ["pellets", get_ref_images(31), "PELLETS"],
        ["patented_impurity_product", get_ref_images(32), "Patented Impurity Product"],
        ["nutraceuticals", get_ref_images(33), "Nutraceuticals"],
        ["nasal_drop_oral_suspensions", get_ref_images(34), "Nasal Drops & Oral Suspensions"],
        ["medical_supplie_Equipment", get_ref_images(35), "Medical Supplies & Equipment"],
        ["injectable_ointments", get_ref_images(36), "Injectable & Ointments"],
    )
    return render(request, "home/dye_and_.html", {"cate_name": "Food & Pharma", "lists": list, "cate_url": "food_and_pharma_sub","details":company_details})


def food_pharma_sub(request, prod_name):
    company_details = M.company_detail.objects.first()
    if prod_name == "veterinary_formulation":
        list = (
            ["poultry_product", get_ref_images(37), "Poultry Products"],
            ["other_product", get_ref_images(38), "Other Products"],
            ["livestock_product", get_ref_images(39), "LiveStock Products"],
            ["companion_animal_products", get_ref_images(40), "Companion Animal Products"],
        )
        return render(request, "home/dye_and_.html", {"cate_name": "Veterinary Formulations", "lists": list, "cate_url": "food_and_pharma_sub","details":company_details})
    elif prod_name == "veterinary_apis":
        data = M.veterinary_apis.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Veterinary Apis", "data": data,"details":company_details})
    elif prod_name == "tablets_capsules":
        list = (
            ["tablet_and_capsules", get_ref_images(41), "Tablets & Capsules"],
            ["combination_formulations", get_ref_images(42), "Combination Formulations"],
        )
        return render(request, "home/dye_and_.html", {"cate_name": "Tablet & Capsules", "lists": list, "cate_url": "food_and_pharma_sub","details":company_details})
    elif prod_name == "reference_std_impurities":
        data = M.ref_std_impurities.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Reference Standards & Impurities", "data": data,"details":company_details})
    elif prod_name == "pellets":
        data = M.pellet.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Pellets", "data": data,"details":company_details})
    elif prod_name == "patented_impurity_product":
        data = M.patented_impurity.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Patented Impurity Products", "data": data,"details":company_details})
    elif prod_name == "nutraceuticals":
        list = (
            ["Stabilized_vitamins", get_ref_images(43), "Stabilized Vitamins"],
            ["Specialities", get_ref_images(44), "Specialities"],
            ["Minerals", get_ref_images(45), "Minerals"],
            ["amino_acid", get_ref_images(46), "Amino Acids"],
        )
        return render(request, "home/dye_and_.html", {"cate_name": "Nutraceuticals", "lists": list, "cate_url": "food_and_pharma_sub","details":company_details})
    elif prod_name == "nasal_drop_oral_suspensions":
        list = (
            ["oral_suspensions",  get_ref_images(47), "Oral Suspension"],
            ["nasal_drop",  get_ref_images(48), "NASAL DROPS"],
        )
        return render(request, "home/dye_and_.html", {"cate_name": "Nasal Drop & Oral Suspensions", "lists": list, "cate_url": "food_and_pharma_sub","details":company_details})
    elif prod_name == "medical_supplie_Equipment":
        data = M.medical_supply_equip.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Medical Supplie & Equipments", "data": data,"details":company_details})
    elif prod_name == "injectable_ointments":
        list = (
            ["ointments",  get_ref_images(49), "ointments"],
            ["injectables",  get_ref_images(50), "Injectables"],
        )
        return render(request, "home/dye_and_.html", {"cate_name": "Injectables & Ointments", "lists": list, "cate_url": "food_and_pharma_sub","details":company_details})
    elif prod_name == "poultry_product":
        data = M.poultry.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Poultry Products", "data": data,"details":company_details})
    elif prod_name == "other_product":
        data = M.other_products.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Other Products", "data": data,"details":company_details})
    elif prod_name == "livestock_product":
        data = M.livestock_product.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Live Stock Products", "data": data,"details":company_details})
    elif prod_name == "companion_animal_products":
        data = M.companion_animal_product.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Companion Animal Product", "data": data,"details":company_details})
    elif prod_name == "tablet_and_capsules":
        data = M.tablet_capsules.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Tablet & Capsules", "data": data,"details":company_details})
    elif prod_name == "combination_formulations":
        data = M.combination_formulations.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Combination Formulations", "data": data,"details":company_details})
    elif prod_name == "Stabilized_vitamins":
        data = M.Stabilized_vitamins.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Stabilized Vitamins", "data": data,"details":company_details})
    elif prod_name == "Specialities":
        data = M.Specialities.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Specialities", "data": data,"details":company_details})
    elif prod_name == "Minerals":
        data = M.Minerals.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Minerals", "data": data,"details":company_details})
    elif prod_name == "amino_acid":
        data = M.amino_acid.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Amino Acid", "data": data,"details":company_details})
    elif prod_name == "oral_suspensions":
        data = M.oral_suspensions.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Oral Suspension", "data": data,"details":company_details})
    elif prod_name == "nasal_drop":
        data = M.nasal_drop.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Nasal Drop", "data": data,"details":company_details})
    elif prod_name == "ointments":
        data = M.ointments.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Ointments", "data": data,"details":company_details})
    elif prod_name == "injectables":
        data = M.injectables.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Injectables", "data": data,"details":company_details})
    # raise 404 for else request

    return HttpResponse(prod_name)


# def food_pharma_sub_prod(request, prod_name, prod_name_sub):
#     return HttpResponse(prod)


def shades_and_pigments(request):
    company_details = M.company_detail.objects.first()
    list = (
        ["waterbase_intjet_ink", get_ref_images(51), "Waterbase inkjet Int"],
        ["universal_stainer", get_ref_images(52), "Universal Stainer"],
        ["paints", get_ref_images(53), "Paints"],
        ["organic_pigment", get_ref_images(54), "Organic Pigment"],
        ["machine_cotaing_colorant", get_ref_images(55), "Machine Cotaing Colorant"],
        ["inorganic_pigment", get_ref_images(56), "Inorganic Pigment"],
        ["industrial_coating", get_ref_images(57), "Industrial Coating"],
        ["cement_architecture_dispersion", get_ref_images(58), "Cement Architecture Dispersion"],
        ["architecture_paint", get_ref_images(59), "Architecture Paints"],
        ["13_waterbase_flexo_ink", get_ref_images(60), "13 Waterbase Flexo ink"],
        ["11_mixed_meta_oxides", get_ref_images(61), "11 Mixed Meta Oxides"],
        ["08_12_pvc_masterbatches", get_ref_images(62), "08 + 12 Pvc and Pvc Master Batches"],
    )
    return render(request, "home/dye_and_.html", {"cate_name": "Shades & Pigments", "lists": list, "cate_url": "shades_and_pigments_sub","details":company_details})


def shades_and_pigments_sub(request, prod_name):
    company_details = M.company_detail.objects.first()
    choices = [
        ("waterbase_intjet_ink", "Waterbase inkjet Int"),
        ("universal_stainer", "Universal Stainer"),
        ("paints", "paints"),
        ("machine_cotaing_colorant", "Machine Cotaing Colorant"),
        ("inorganic_pigment", "Inorganic Pigment"),
        ("industrial_coating", "Industrial Coating"),
        ("cement_architecture_dispersion", "Cement Architecture Dispersion"),
        ("architecture_paint", "Architecture Paints"),
        ("13_waterbase_flexo_ink", "13 Waterbase Flexo ink"),
        ("11_mixed_meta_oxides", "11 Mixed Meta Oxides"),
        ("08_12_pvc_masterbatches", "08 + 12 Pvc and Pvc Master Batches"),
        ("toner_fanal_pigment","Toner Fanal Pigments"),
        ("hign_performance_pigment","High Performance Pigments"),
    ]
    if prod_name == "organic_pigment":
        list = (
            ["toner_fanal_pigment", get_ref_images(63), "Toner Fanal Pigments"],
            ["hign_performance_pigment", get_ref_images(64), "High Performance Pigments"],
            ["flouroscent_pigments", get_ref_images(65), "Flouroscent Pigments"],
        )
        return render(request, "home/dye_and_.html", {"cate_name": "Organic Pigments", "lists": list, "cate_url": "shades_and_pigments_sub","details":company_details})
    
    elif prod_name == "flouroscent_pigments":
        data = M.flouroscent_pigments.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Flouroscent Pigments", "data": data,"details":company_details})
    else:
        for choice in choices:
            if prod_name == choice[0]:
                data = M.shades_and_pigment.objects.filter(type=prod_name)
                return render(request, "home/product_table.html", {"product_name": choice[1], "data": data,"shades_pigment_common":True,"details":company_details})
    return HttpResponse(prod_name)


def varieties_and_cosmetics(request):
    company_details = M.company_detail.objects.first()
    images = []
    for i in (12,13,14):
        images.append(get_ref_images(i))
    return render(request, "home/dye_and_.html", {"cate_name": "var_cosmetics","details":company_details,"cate_images":images})


def intermediates_desc(request):
    company_details = M.company_detail.objects.first()
    data = M.intermediates.objects.all()
    compounds = M.intermediates.objects.values_list('compound').distinct()
    compounds = set(list(compounds))
    return render(request, "home/product_table.html", {"product_name": "intermediates", "data": data,"details":company_details,"compounds":compounds})


def acid_dyes_sub(request):
    company_details = M.company_detail.objects.first()
    list = (
            ["mill_dyes", get_ref_images(66), "Milling Dyes"],
            ["leveling_dyes", get_ref_images(67), "Levelling Dyes"],
            ["acid_dyes", get_ref_images(68), "Acid Dyes"],
            ["1_1_metal_complex_dyes", get_ref_images(69), "1 1 METAL COMPLEX DYES"],
            ["1_2_metal_complex_dyes", get_ref_images(70), "1 2 METAL COMPLEX DYES"],
                )
    return render(request, "home/dye_and_.html", {"cate_name": "Acid Dyes", "lists": list,"cate_url": "acid_dyes_sub_tables","details":company_details})

def acid_dyes_sub_tables(request,prod_name):
    company_details = M.company_detail.objects.first()
    if prod_name == "mill_dyes":
        data = M.mill_dyes.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Mill Dyes", "data": data,"details":company_details})
    elif prod_name == "leveling_dyes":
        data = M.mill_dyes.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Levelling Dyes", "data": data,"details":company_details})
    elif prod_name == "acid_dyes":
        data = M.acid_dyes_sub.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Acid Dyes", "data": data,"details":company_details})
    elif prod_name == "1_1_metal_complex_dyes":
        data = M.metal_complex_dyes.objects.filter(type=prod_name)
        return render(request, "home/product_table.html", {"product_name": "1 1 METAL COMPLEX DYES", "data": data,"details":company_details})
    elif prod_name == "1_2_metal_complex_dyes":
        data = M.metal_complex_dyes.objects.filter(type=prod_name)
        return render(request, "home/product_table.html", {"product_name": "1 2 METAL COMPLEX DYES", "data": data,"details":company_details})
    return HttpResponse(prod_name)


def acid_dyes_list(request):
    company_details = M.company_detail.objects.first()
    data = M.acid_dyes.objects.all()
    return render(request, "home/product_table.html", {"product_name": "acid_dyes", "data": data,"details":company_details})

def basic_dyes(request):
    company_details = M.company_detail.objects.first()
    list = (
            ["basic_dyes_liquid", get_ref_images(71), "Liquid"],
            ["basic_dyes_powder", get_ref_images(72), "Powder"],
            )
    return render(request, "home/dye_and_.html", {"cate_name": "Basic Dyes", "lists": list,"cate_url": "basic_dyes_sub","details":company_details})

def basic_dyes_sub(request,prod_name):
    company_details = M.company_detail.objects.first()
    if prod_name == "basic_dyes_liquid":
        data = M.basic_dyes.objects.filter(type = "L")
        return render(request, "home/product_table.html", {"product_name": "Basic Dyes Liquid", "data": data,"details":company_details})
    elif prod_name =="basic_dyes_powder":
        data = M.basic_dyes.objects.filter(type = "P")
        return render(request, "home/product_table.html", {"product_name": "Basic Dyes Powder", "data": data,"details":company_details})
def basic_dyes_liquid(request):
    company_details = M.company_detail.objects.first()
    data = M.basic_dyes.objects.all()
    return render(request, "home/product_table.html", {"product_name": "basic_dyes", "data": data,"details":company_details})

def direct_dyes_list(request):
    company_details = M.company_detail.objects.first()
    data = M.direct_dyes.objects.all()
    return render(request, "home/product_table.html", {"product_name": "Direct Dyes", "data": data,"details":company_details})


def food_lake_color_list(request):
    company_details = M.company_detail.objects.first()
    list = (
            ["blended_color", get_ref_images(73), "Blended Color"],
            ["D_C_color", get_ref_images(74), "D & C Color"],
            ["FD_C_color", get_ref_images(75), "FD & C Color"],
            ["Food_color", get_ref_images(76), "Food  Color"],
            ["lake_color", get_ref_images(77), "Lake Color"],
            )
    return render(request, "home/dye_and_.html", {"cate_name": "Basic Dyes", "lists": list,"cate_url": "food_lake_sub","details":company_details})

def food_lake_sub(request,prod_name):
    company_details = M.company_detail.objects.first()
    if prod_name == "blended_color":
        data = M.blended_color.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Blended Color", "data": data,"details":company_details})
    elif prod_name == "D_C_color":
        data = M.D_C_color.objects.all()
        return render(request, "home/product_table.html", {"product_name": "D & C Color", "data": data,"details":company_details})
    elif prod_name == "FD_C_color":
        data = M.FD_c_color.objects.all()
        return render(request, "home/product_table.html", {"product_name": "FD & C Color", "data": data,"details":company_details})
    elif prod_name == "Food_color":
        data = M.food_color.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Food Color", "data": data,"details":company_details})
    elif prod_name == "lake_color":
        data = M.lake_color_dyes.objects.all()
        return render(request, "home/product_table.html", {"product_name": "Lake Color", "data": data,"details":company_details})
    return HttpResponse(prod_name)



def solvent_dyes_list(request):
    company_details = M.company_detail.objects.first()
    data = M.solvet_dyes.objects.all()
    return render(request, "home/product_table.html", {"product_name": "solvent_dyes", "data": data,"details":company_details})


def reactive_me_dyes_list(request):
    company_details = M.company_detail.objects.first()
    list = (
            ["HE_dyes", get_ref_images(78), "Reactice He Dyes"],
            ["Hot_dyes", get_ref_images(79), "Reactice Hot Dyes"],
            ["ME_dyes", get_ref_images(80), "Reactice Me Dyes"],
            ["printing_dyes_1", get_ref_images(81), "Reactice Printing  Dyes 1"],
            ["printing_dyes_2", get_ref_images(82), "Reactice Printing  Dyes 2"],
            ["vinyl_sulphone_base_dye", get_ref_images(83), "REACTIVE VINYL SULPHONE BASE DYE"],
            )
    return render(request, "home/dye_and_.html", {"cate_name": "REACTIVE DYES", "lists": list,"cate_url": "reactive_dyes_sub","details":company_details})

def reactive_dyes_sub(request,prod_name):
    company_details = M.company_detail.objects.first()
    data = M.reactive_dyes.objects.filter(type=prod_name)
    try:
        return render(request, "home/product_table.html", {"product_name": data[0].get_type_display(), "data": data,"flag":"reactive_dyes","details":company_details})
    except Exception as e:
        print(e)
        return render(request, "home/product_table.html", {"product_name": "No Data", "data": data,"flag":"reactive_dyes","details":company_details})


def D_C_color(request):
    company_details = M.company_detail.objects.first()
    data = M.D_C_color.objects.all()
    return render(request, "home/product_table.html", {"product_name": "D_C_color", "data": data,"details":company_details})


def Lake_color(request):
    company_details = M.company_detail.objects.first()
    data = M.lake_color.objects.all()
    return render(request, "home/product_table.html", {"product_name": "lake_color", "data": data,"details":company_details})


def ess_oil_list(request):
    company_details = M.company_detail.objects.first()
    list_of_oils = [
        {"name": "Anti Bacterial Oil", "ref_url": "esse_oil_list_sub",
            "ref_img": get_ref_images(15), "oil_type": "ant_bac"},
        {"name": "antiviral Oil", "ref_url": "esse_oil_list_sub",
            "ref_img": get_ref_images(16), "oil_type": "anti_"},
        {"name": "carrier Oil", "ref_url": "esse_oil_list_sub",
            "ref_img": get_ref_images(17), "oil_type": "carrier"},
        {"name": "Clay & Butter Oil", "ref_url": "esse_oil_list_sub",
            "ref_img": get_ref_images(18), "oil_type": "C_B"},
        {"name": "Fragrance Oil", "ref_url": "esse_oil_list_sub",
            "ref_img": get_ref_images(19), "oil_type": "Frag"},
        {"name": "Herbal Oil", "ref_url": "esse_oil_list_sub",
            "ref_img": get_ref_images(20), "oil_type": "herb"},
        {"name": "Natural Essential Oil", "ref_url": "esse_oil_list_sub",
            "ref_img": get_ref_images(21), "oil_type": "N_E"},
        {"name": "Nature Identical Oils", "ref_url": "esse_oil_list_sub",
            "ref_img": get_ref_images(22), "oil_type": "N_i"},
        {"name": "Organic Cold Pressed Oils", "ref_url": "esse_oil_list_sub",
            "ref_img": get_ref_images(23), "oil_type": "org_cold_press"},
        {"name": "Organic Essential Oils", "ref_url": "esse_oil_list_sub",
            "ref_img": get_ref_images(24), "oil_type": "org_ess_oil"},

    ]
    images = []
    for i in (25,26):
        images.append(get_ref_images(i))
    return render(request, "home/dye_and_.html", {"cate_name": "esse_oils", "oils_name": list_of_oils,"details":company_details,"cate_images":images})


def ess_basic_oil(request, oil_name):
    company_details = M.company_detail.objects.first()
    try:
        data = M.essential_oil.objects.filter(oil_type=oil_name)
        return render(request, "home/product_table.html", {"product_name": "ess_base_oil", "data": data, "oil_name": str(data[0].get_oil_type_display()),"details":company_details})
    except Exception as e:
        return render(request, "home/product_table.html", {"product_name": "ess_base_oil", "data": data, "oil_name": "No data","details":company_details})


def oleoresin_oil(request):
    company_details = M.company_detail.objects.first()
    data = M.oleoresin_oil.objects.all()
    return render(request, "home/product_table.html", {"product_name": "oleoresin", "data": data, "oil_name": "Oleoresin Oil","details":company_details})


def natural_flower_oil(request):
    company_details = M.company_detail.objects.first()
    data = M.natural_flower_oil.objects.all()
    return render(request, "home/product_table.html", {"product_name": "natural_flower", "data": data, "oil_name": "Natural Flower Oil","details":company_details})


def import_data(request):    
    with open("../../Kewin Chemicals Website Data/Kewin Chemicals - Products Data Sheet/DYES _ INTERMEDIATES DIVISION/SOLVENT DYES/SOLVENT DYES.csv", "r") as file:
        csv_file = read_csv(file)
        for i in csv_file.iterrows():
            print(i[0])
            obj = M.solvet_dyes()
            obj.product_name = i[1][0]
            obj.case_no = i[1][1]
            obj.save()
    return HttpResponse("done")

def search_filter(request):
    search_values = []
    if request.is_ajax():
        temp_list = M.intermediates.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/intermediates_list","Intermediates"))
            search_values.extend(iterate_obj_name(temp_list,"/intermediates_list","Intermediates"))
        temp_list = M.mill_dyes.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/acid_dyes/mill_dyes","Mill Dyes"))
        temp_list = M.leveling_dyes.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/acid_dyes/leveling_dyes","Leveling Dyes"))
        temp_list = M.acid_dyes_sub.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/acid_dyes/acid_dyes","Acide Dyes"))
        temp_list = M.metal_complex_dyes.objects.filter(type="1_1_metal_complex_dyes")
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/acid_dyes/1_1_metal_complex_dyes","1 1 Metal Complex Dyes"))
        temp_list = M.metal_complex_dyes.objects.filter(type="1_2_metal_complex_dyes")
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/acid_dyes/1_2_metal_complex_dyes","1 2 Metal Complex Dyes"))
        temp_list = M.basic_dyes.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/basic_dyes","Basic Dyes"))
        temp_list = M.direct_dyes.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/direct_dyes_list","Direct Dyes"))
        temp_list = M.blended_color.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/food_lake_sub/blended_color","Blended Color"))
            search_values.extend(iterate_obj_name(temp_list,"/food_lake_sub/blended_color","Blended Color"))
        temp_list = M.food_color.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/food_lake_sub/Food_color","Food color"))
            search_values.extend(iterate_obj_name(temp_list,"/food_lake_sub/Food_color","Food color"))
        temp_list = M.lake_color_dyes.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/food_lake_sub/lake_color","Lake Color"))
            search_values.extend(iterate_obj_name(temp_list,"/food_lake_sub/lake_color","Lake Color"))
        temp_list = M.solvet_dyes.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/solvent_dyes_list","Solvent Dyes"))
            search_values.extend(iterate_obj_name(temp_list,"/solvent_dyes_list","Solvent Dyes"))
        choice =[
        ("HE_dyes","Reactice He Dyes"),
        ("Hot_dyes","Reactice Hot Dyes"),
        ("ME_dyes","Reactice Me Dyes"),
        ("printing_dyes_1","Reactice Printing  Dyes 1"),
        ("printing_dyes_2","Reactice Printing  Dyes 2"),
        ("vinyl_sulphone_base_dye","REACTIVE VINYL SULPHONE BASE DYE"),
        ]
        for i in choice:
            temp_list = M.reactive_dyes.objects.filter(type=i[0])
            if len(temp_list) > 0:
                search_values.extend(iterate_obj(temp_list,"/reactive_dyes_sub/{}".format(i[0]),i[1]))
                search_values.extend(iterate_obj_name(temp_list,"/reactive_dyes_sub/{}".format(i[0]),i[1]))
        temp_list = M.oleoresin_oil.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/oleoresin_oil","Oleoresin Oil"))
            search_values.extend(iterate_obj_name(temp_list,"/oleoresin_oil","Oleoresin Oil"))
        temp_list = M.natural_flower_oil.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/natural_flower_oil","Natural Flower Oil"))
            search_values.extend(iterate_obj_name(temp_list,"/natural_flower_oil","Natural Flower Oil"))
        temp_list = M.veterinary_apis.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/Food_and_pharma/veterinary_apis","Veterinary Apis"))
        temp_list = M.ref_std_impurities.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/Food_and_pharma/ref_std_impurities","Ref std Impurities"))
        temp_list = M.pellet.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/Food_and_pharma/pellets","Pellets"))
        temp_list = M.patented_impurity.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/Food_and_pharma/patented_impurity_product","Patented Impurity"))
        temp_list = M.Stabilized_vitamins.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/Food_and_pharma/Stabilized_vitamins","Stabilized Vitamins"))
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/Stabilized_vitamins","Stabilized Vitamins"))
        temp_list = M.Specialities.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/Food_and_pharma/Specialities","Specialities"))
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/Specialities","Specialities"))
        temp_list = M.Minerals.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/Food_and_pharma/Minerals","Minerals"))
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/Minerals","Minerals"))
        temp_list = M.amino_acid.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj(temp_list,"/Food_and_pharma/amino_acid","Amino Acid"))
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/amino_acid","Amino Acid"))
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
        for i in choices:
            temp_list = M.shades_and_pigment.objects.filter(type=i[0])
            if len(temp_list) > 0:
                search_values.extend(iterate_obj(temp_list,"/shades_and_pigment/{}".format(i[0]),i[1]))
                search_values.extend(iterate_obj_name(temp_list,"/shades_and_pigment/{}".format(i[0]),i[1]))
        temp_list = M.medical_supply_equip.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/medical_supplie_Equipment","Medical Supplie"))
        temp_list = M.poultry.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/poultry_product","Poultry Product"))
        temp_list = M.livestock_product.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/livestock_product","Livestock Product"))
        temp_list = M.companion_animal_product.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/companion_animal_products","Companion animal"))
        temp_list = M.tablet_capsules.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/tablet_and_capsules","Tablet & Capsules"))
        temp_list = M.combination_formulations.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/combination_formulations","Combination Formulations"))
        temp_list = M.oral_suspensions.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/oral_suspensions","Oral Suspensions"))
        temp_list = M.nasal_drop.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/nasal_drop","Nasal Drop"))
        temp_list = M.ointments.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/ointments","Ointments"))
        temp_list = M.injectables.objects.all()
        if len(temp_list) > 0:
            search_values.extend(iterate_obj_name(temp_list,"/Food_and_pharma/injectables","Injectables"))
        search_values.append({"value":"Dyes & intermidiate","data":{"url":"/dye_and_intermediates","category":"Main Category"}})
        search_values.append({"value":"Food & Pharma","data":{"url":"/Food_and_pharma","category":"Main Category"}})
        search_values.append({"value":"Shades & Pigments","data":{"url":"/shades_and_pigments","category":"Main Category"}})
        search_values.append({"value":"Varieties & Cosmetics","data":{"url":"/varieties_and_cosmetics","category":"Main Category"}})
    return JsonResponse({"values":search_values})

def iterate_obj(query_set,url,categoty):
    temp_arr = []
    for obj  in query_set:
        if len(obj.case_no) > 2:
            temp_arr.append({"value":obj.case_no,"data":{"url":url,"category":categoty}})
    return temp_arr


def iterate_obj_name(query_set,url,categoty):
    temp_arr = []
    for obj  in query_set:
        if len(obj.product_name) > 2:
            temp_arr.append({"value":obj.product_name,"data":{"url":url,"category":categoty}})
    return temp_arr

def free_sample(request):
    try:
        obj = M.user_Requirement()
        obj.Full_name = request.POST['Full_name']
        obj.email_id = request.POST['email_id']
        obj.mobile_number = request.POST['mobile_number']
        obj.Requirement_file = request.FILES['file']
        obj.save()
        user_requirement_send_mail_to_admin([obj.Full_name,obj.mobile_number,obj.email_id],obj.Requirement_file)
        if user_requirement_send_mail_to_client(obj.email_id,obj.Requirement_file):
            return HttpResponse("1")
        else:
            return HttpResponse("-1")
    except:
        return HttpResponse("-1")
    return HttpResponse("-1")
def create_mail_config():
    from_mail = M.company_detail.objects.all()[0].sales_department_email_id
    from_mail_pass = M.company_detail.objects.all()[0].sales_department_email_id_pass
    print(from_mail)
    print(from_mail_pass)
    backend = EmailBackend(host=settings.EMAIL_HOST,port=settings.EMAIL_PORT,username=from_mail,password=from_mail_pass,use_tls=settings.EMAIL_USE_TLS)
    return backend
def user_requirement_send_mail_to_client(user_mail,requirement_file):
    try:
        subject = "Kewin Chemical Free Sample Requirement"
        message = "Thank You For Visit. We Full Fill Your Requirement Very Soon."
        backend = create_mail_config()
        print(backend)
        email = EmailMessage(
        subject=subject,
        body=message,
        to=[user_mail],
        connection=backend
        )
        email.attach("Free Sample Requirement.csv",requirement_file.open().read(),mimetype='text/csv')
        email.send()
        return True
    except Exception as e:
        print(e)
        return False
def user_requirement_send_mail_to_admin(client_data,requirement_file):
    try:
        subject = "Client Free Sample Requirement."
        message = "{} Request for Free Sample \n Name: {} \n Mobile Number: {} \n Email Id: {} \n".format(client_data[0],client_data[0],client_data[1],client_data[2])
        to_mail = M.company_detail.objects.all()[0].customer_care_Email_Id
        backend = create_mail_config()
        print(backend)
        email = EmailMessage(
        subject=subject,
        body=message,
        to=[to_mail],
        connection=backend
        )
        email.attach("Free Sample Requirement.csv",requirement_file.open().read(),mimetype='text/csv')
        email.send()
        return True
    except Exception as e:
        print(e)
        return False

def user_query_send(subject,message,to_mail_id):
    try:
        backend = create_mail_config()
        print(backend)
        email = EmailMessage(
        subject=subject,
        body=message,
        to=[to_mail_id],
        connection=backend
        )
        email.send()
        return True
    except Exception as e:
        print(e)
        return False




def color_set(request):
    try:    
        with open("{}/home/colors.txt".format(settings.BASE_DIR),"r") as file:
            all = M.acid_dyes_sub.objects.all();
            for (i,color) in enumerate(file.readlines()):
                print(i)
                print(color)
                
        
        return HttpResponse("done")
    except Exception as e:
        print(e)
        return HttpResponse("error")


