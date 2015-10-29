import pandas as pd

#######################
##
##  import files to analyze
##
#######################

demo = pd.read_csv("pop_zip.csv")
bus = pd.read_csv("ny_bus.csv")

#######################
##
##  generalize categories
##
#######################

import json
with open("category.json") as data_file:
    cat = json.load(data_file)

dict_conv = {}
for al_dict in cat:
    dict_conv[al_dict["alias"]] = al_dict["title"]
    dict_conv[al_dict["title"]] = al_dict["title"]
    for i in al_dict["category"]:
        dict_conv[i["alias"]] = al_dict["title"]
        dict_conv[i["title"]] = al_dict["title"]
        for j in i["category"]:
            dict_conv[j["alias"]] = al_dict["title"]
            dict_conv[j["title"]] = al_dict["title"]

def new_cat(bus_cat):
    if bus_cat=='dominican':
        new_cat = "Restaurants"
    elif bus_cat=="trainstations":
        new_cat = "Public Services & Government"
    elif bus_cat=="giftshops":
        new_cat = "Shopping"
    elif bus_cat=="mobilephonerepair":
        new_cat = "Local Services"
    elif bus_cat=="hairstylists":
        new_cat = "Beauty and Spas"  
    elif bus_cat=="glassandmirrors":
        new_cat = "Shopping" 
    elif bus_cat=="foodtrucks":
        new_cat = "Restaurants"
    elif bus_cat=="security":
        new_cat = "Professional Services"
    elif bus_cat=="vitaminssupplements":
        new_cat = "Health and Medical"
    elif bus_cat=="sugaring":
        new_cat = "Beauty and Spas"
    elif bus_cat=="wheelrimrepair":
        new_cat = "Automotive"    
    elif bus_cat=="diagnosticservices":
        new_cat = "Health and Medical"  
    elif bus_cat=="cocktailbars":
        new_cat = "Nightlife"  
    elif bus_cat=="csa":
        new_cat = "Food"  
    elif bus_cat=="fireprotection":
        new_cat = "Public Services & Government"  
    elif bus_cat=="eventphotography":
        new_cat = "Professional Services" 
    elif bus_cat=="blowoutservices":
        new_cat = "Home Services"
    elif bus_cat=="cprclasses":
        new_cat = "Education"
    elif bus_cat=="cantonese":
        new_cat = "Restaurants"
    elif bus_cat=="transmissionrepair":
        new_cat = "Automotive"
    elif bus_cat=="fleamarkets":
        new_cat = "Shopping"
    elif bus_cat=="autoloanproviders":
        new_cat = "Financial Services"
    elif bus_cat=="refinishing":
        new_cat = "Home Services"
    elif bus_cat=="ticketsales":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="firedepartments":
        new_cat = "Public Services & Government"
    elif bus_cat=="shredding":
        new_cat = "Local Services"
    elif bus_cat=="damagerestoration":
        new_cat = "Financial Services"
    elif bus_cat=="paintstores":
        new_cat = "Local Services"
    elif bus_cat=="brewingsupplies":
        new_cat = "Shopping"
    elif bus_cat=="signmaking":
        new_cat = "Professional Services"
    elif bus_cat=="partyequipmentrentals":
        new_cat = "Local Services"
    elif bus_cat=="waxing":
        new_cat = "Beauty and Spas"
    elif bus_cat=="legalservices":
        new_cat = "Professional Services"
    elif bus_cat=="occupationaltherapy":
        new_cat = "Health and Medical"
    elif bus_cat=="partybusrentals":
        new_cat = "Event Planning & Services"
    elif bus_cat=="communitycenters":
        new_cat = "Local Services"
    elif bus_cat=="commercialrealestate":
        new_cat = "Real Estate"
    elif bus_cat=="comfortfood":
        new_cat = "Restaurants"
    elif bus_cat=="reiki":
        new_cat = "Health and Medical"
    elif bus_cat=="autocustomization":
        new_cat = "Automotive"
    elif bus_cat=="trinidadian":
        new_cat = "Restaurants"
    elif bus_cat=="uniforms":
        new_cat = "Shopping"
    elif bus_cat=="taxlaw":
        new_cat = "Public Services & Government"
    elif bus_cat=="firstaidclasses":
        new_cat = "Education"
    elif bus_cat=="gutterservices":
        new_cat = "Local Services"
    elif bus_cat=="diagnosticimaging":
        new_cat = "Health and Medical"
    elif bus_cat=="irish_pubs":
        new_cat = "Nightlife"
    elif bus_cat=="videogamestores":
        new_cat = "Shopping"
    elif bus_cat=="chickenshop":
        new_cat = "Restaurants"
    elif bus_cat=="doorsales":
        new_cat = "Event Planning & Services"
    elif bus_cat=="pianoservices":
        new_cat = "Professional Services"
    elif bus_cat=="powdercoating":
        new_cat = "Local Services"
    elif bus_cat=="trophyshops":
        new_cat = "Shopping"
    elif bus_cat=="tanningbeds":
        new_cat = "Beauty and Spas"
    elif bus_cat=="waterdelivery":
        new_cat = "Local Services"
    elif bus_cat=="medicaltransportation":
        new_cat = "Health and Medical"
    elif bus_cat=="bangladeshi":
        new_cat = "Restaurants"
    elif bus_cat=="photoboothrentals":
        new_cat = "Event Planning & Services"
    elif bus_cat=="sessionphotography":
        new_cat = "Professional Services"
    elif bus_cat=="psychologists":
        new_cat = "Professional Services"
    elif bus_cat=="vapeshops":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="menshair":
        new_cat = "Beauty and Spas"
    elif bus_cat=="senegalese":
        new_cat = "Beauty and Spas"
    elif bus_cat=="utilities":
        new_cat = "Shopping"
    elif bus_cat=="walkingtours":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="poledancingclasses":
        new_cat = "Education"
    elif bus_cat=="pretzels":
        new_cat = "Food"
    elif bus_cat=="hennaartists":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="cabinetry":
        new_cat = "Home Services"
    elif bus_cat=="culturalcenter":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="organic_stores":
        new_cat = "Food"
    elif bus_cat=="haitian":
        new_cat = "Restaurants"
    elif bus_cat=="bartenders":
        new_cat = "Professional Services"
    elif bus_cat=="arabian":
        new_cat = "Restaurants"
    elif bus_cat=="knifesharpening":
        new_cat = "Professional Services"
    elif bus_cat=="cupcakes":
        new_cat = "Food"
    elif bus_cat=="sharedofficespaces":
        new_cat = "Real Estate"
    elif bus_cat=="facepainting":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="medicalsupplies":
        new_cat = "Health and Medical"
    elif bus_cat=="spraytanning":
        new_cat = "Beauty and Spas"
    elif bus_cat=="hypnosis":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="lebanese":
        new_cat = "Restaurants"
    elif bus_cat=="gymnastics":
        new_cat = "Active Life"
    elif bus_cat=="falafel":
        new_cat = "Restaurants"
    elif bus_cat=="shanghainese":
        new_cat = "Restaurants"
    elif bus_cat=="uzbek":
        new_cat = "Restaurants"
    elif bus_cat=="jetskis":
        new_cat = "Shopping"
    elif bus_cat=="hotpot":
        new_cat = "Restaurants"
    elif bus_cat=="food_court":
        new_cat = "Restaurants"
    elif bus_cat=="bubbletea":
        new_cat = "Food"
    elif bus_cat=="pressurewashers":
        new_cat = "Home Services"
    elif bus_cat=="pastashops":
        new_cat = "Food"
    elif bus_cat=="winetours":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="surgeons":
        new_cat = "Health and Medical"
    elif bus_cat=="hats":
        new_cat = "Shopping"
    elif bus_cat=="formalwear":
        new_cat = "Shopping"
    elif bus_cat=="ramen":
        new_cat = "Restaurants"
    elif bus_cat=="basketballcourts":
        new_cat = "Active Life"
    elif bus_cat=="bespoke":
        new_cat = "Professional Services"
    elif bus_cat=="lactationservices":
        new_cat = "Health and Medical"
    elif bus_cat=="insulationinstallation":
        new_cat = "Professional Services"
    elif bus_cat=="mohels":
        new_cat = "Health and Medical"
    elif bus_cat=="radiologists":
        new_cat = "Health and Medical"
    elif bus_cat=="countryclubs":
        new_cat = "Event Planning & Services"
    elif bus_cat=="challengecourses":
        new_cat = "Education"
    elif bus_cat=="races":
        new_cat = "Active Life"
    elif bus_cat=="marinas":
        new_cat = "Active Life"
    elif bus_cat=="businesslawyers":
        new_cat = "Professional Services"
    elif bus_cat=="bootcamps":
        new_cat = "Education"
    elif bus_cat=="datarecovery":
        new_cat = "Professional Services"
    elif bus_cat=="poolservice":
        new_cat = "Local Services"
    elif bus_cat=="furnitureassembly":
        new_cat = "Home Services"
    elif bus_cat=="duilawyers":
        new_cat = "Professional Services"
    elif bus_cat=="artclasses":
        new_cat = "Education"
    elif bus_cat=="cafeteria":
        new_cat = "Restaurants"
    elif bus_cat=="talentagencies":
        new_cat = "Professional Services"
    elif bus_cat=="chimneysweeps":
        new_cat = "Home Services"
    elif bus_cat=="trains":
        new_cat = "Public Services & Government"
    elif bus_cat=="telecommunications":
        new_cat = "Professional Services"
    elif bus_cat=="goldbuyers":
        new_cat = "Professional Services"
    elif bus_cat=="translationservices":
        new_cat = "Professional Services"
    elif bus_cat=="liceservices":
        new_cat = "Home Services"
    elif bus_cat=="kiteboarding":
        new_cat = "Active Life"
    elif bus_cat=="collegecounseling":
        new_cat = "Professional Services"
    elif bus_cat=="fencesgates":
        new_cat = "Home Services"
    elif bus_cat=="vehicleshipping":
        new_cat = "Automotive"
    elif bus_cat=="barreclasses":
        new_cat = "Education"
    elif bus_cat=="distilleries":
        new_cat = "Food"
    elif bus_cat=="doulas":
        new_cat = "Professional Services"
    elif bus_cat=="cookingclasses":
        new_cat = "Education"
    elif bus_cat=="austrian":
        new_cat = "Restaurants"
    elif bus_cat=="salvadoran":
        new_cat = "Restaurants"
    elif bus_cat=="gelato":
        new_cat = "Food"
    elif bus_cat=="colombian":
        new_cat = "Restaurants"
    elif bus_cat=="poutineries":
        new_cat = "Food"
    elif bus_cat=="guitarstores":
        new_cat = "Shopping"
    elif bus_cat=="cyclingclasses":
        new_cat = "Shopping"
    elif bus_cat=="mailboxcenters":
        new_cat = "Local Services"
    elif bus_cat=="motorcyclinggear":
        new_cat = "Automotive"
    elif bus_cat=="arttours":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="boxing":
        new_cat = "Active Life"
    elif bus_cat=="yelpevents":
        new_cat = "Event Planning & Services"
    elif bus_cat=="kids_activities":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="machinerental":
        new_cat = "Local Services"
    elif bus_cat=="czech":
        new_cat = "Restaurants"
    elif bus_cat=="metalfabricators":
        new_cat = "Professional Services"
    elif bus_cat=="puertorican":
        new_cat = "Restaurants"
    elif bus_cat=="shavedice":
        new_cat = "Food"
    elif bus_cat=="venezuelan":
        new_cat = "Restaurants"
    elif bus_cat=="supperclubs":
        new_cat = "Restaurants"
    elif bus_cat=="payroll":
        new_cat = "Financial Services"
    elif bus_cat=="musicians":
        new_cat = "Professional Services"
    elif bus_cat=="beergardens":
        new_cat = "Nightlife"
    elif bus_cat=="custommerchandise":
        new_cat = "Shopping"
    elif bus_cat=="southafrican":
        new_cat = "Restaurants"
    elif bus_cat=="daycamps":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="communitygardens":
        new_cat = "Local Flavor"
    elif bus_cat=="currencyexchange":
        new_cat = "Financial Services"
    elif bus_cat=="srilankan":
        new_cat = "Restaurants"
    elif bus_cat=="tenantlaw":
        new_cat = "Public Services & Government"
    elif bus_cat=="laboratorytesting":
        new_cat = "Health and Medical"
    elif bus_cat=="pianobars":
        new_cat = "Nightlife"
    elif bus_cat=="childbirthedu":
        new_cat = "Education"
    elif bus_cat=="colonics":
        new_cat = "Beauty and Spas"
    elif bus_cat=="urologists":
        new_cat = "Professional Services"
    elif bus_cat=="appraisalservices":
        new_cat = "Professional Services"
    elif bus_cat=="jewelryrepair":
        new_cat = "Professional Services"
    elif bus_cat=="golflessons":
        new_cat = "Education"
    elif bus_cat=="firewood":
        new_cat = "Home Services"
    elif bus_cat=="armenian":
        new_cat = "Restaurants"
    elif bus_cat=="permanentmakeup":
        new_cat = "Beauty and Spas"
    elif bus_cat=="observatories":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="macarons":
        new_cat = "Food"
    elif bus_cat=="courthouses":
        new_cat = "Public Services & Government"
    elif bus_cat=="laotian":
        new_cat = "Restaurants"
    elif bus_cat=="rugs":
        new_cat = "Home Services"
    elif bus_cat=="skateshops":
        new_cat = "Shopping"
    elif bus_cat=="egyptian":
        new_cat = "Restaurants"
    elif bus_cat=="blooddonation":
        new_cat = "Health and Medical"
    elif bus_cat=="homeinsurance":
        new_cat = "Financial Services"
    elif bus_cat=="matchmakers":
        new_cat = "Professional Services"
    elif bus_cat=="australian":
        new_cat = "Restaurants"
    elif bus_cat=="teppanyaki":
        new_cat = "Restaurants"
    elif bus_cat=="buses":
        new_cat = "Public Services & Government"
    elif bus_cat=="architecturaltours":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="orthotics":
        new_cat = "Health and Medical"
    elif bus_cat=="planetarium":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="fencing":
        new_cat = "Active Life"
    elif bus_cat=="cabaret":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="religiousschools":
        new_cat = "Education"
    elif bus_cat=="editorialservices":
        new_cat = "Professional Services"
    elif bus_cat=="rhematologists":
        new_cat = "Health and Medical"
    elif bus_cat=="aquariumservices":
        new_cat = "Professional Services"
    elif bus_cat=="tiling":
        new_cat = "Home Services"
    elif bus_cat=="homewindowtinting":
        new_cat = "Home Services"
    elif bus_cat=="anesthesiologists":
        new_cat = "Health and Medical"
    elif bus_cat=="paintandsip":
        new_cat = "Home Services"
    elif bus_cat=="hearingaidproviders":
        new_cat = "Health and Medical"
    elif bus_cat=="mobilityequipment":
        new_cat = "Health and Medical"
    elif bus_cat=="wigs":
        new_cat = "Beauty and Spas"
    elif bus_cat=="dialysisclinics":
        new_cat = "Health and Medical"
    elif bus_cat=="airportlounges":
        new_cat = "Restaurants"
    elif bus_cat=="homeautomation":
        new_cat = "Home Services"
    elif bus_cat=="parentingclasses":
        new_cat = "Education"
    elif bus_cat=="popupshops":
        new_cat = "Shopping"
    elif bus_cat=="petadoption":
        new_cat = "Pets"
    elif bus_cat=="skishops":
        new_cat = "Shopping"
    elif bus_cat=="taxidermy":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="musicproduction":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="paddleboarding":
        new_cat = "Active Life"
    elif bus_cat=="bingo":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="registrationservices":
        new_cat = "Local Services"
    elif bus_cat=="ethicgrocery":
        new_cat = "Food"
    elif bus_cat=="carbuyers":
        new_cat = "Automotive"
    elif bus_cat=="personalassistants":
        new_cat = "Professional Services"
    elif bus_cat=="battingcages":
        new_cat = "Active Life"
    elif bus_cat=="racetracks":
        new_cat = "Active Life"
    elif bus_cat=="autoinsurance":
        new_cat = "Financial Services"
    elif bus_cat=="foodtours":
        new_cat = "Arts & Entertainment"
    elif bus_cat=="embroideryandcrochet":
        new_cat = "Professional Services"
    elif bus_cat=="demolitionservices":
        new_cat = "Professional Services"
    elif bus_cat=="valetservices":
        new_cat = "Hotels & Travel"
    elif bus_cat=="bartendingschools":
        new_cat = "Education"
    elif bus_cat=="christmastrees":
        new_cat = "Shopping"
    elif bus_cat=="lasertag":
        new_cat = "Arts & Entertainment"
    else:
        new_cat = dict_conv[bus_cat]
    return new_cat

#######################
##
##  
##
#######################

bus_trial = bus
bus_trial["categories"]=bus_trial.categories.apply(lambda bus_cat: [x.strip("[]").split(',')[-1].strip() for x in bus_cat.split("], [")])
bus_trial["new_categories"]=bus_trial.categories.apply(lambda bus_cat: new_cat(bus_cat[0]))

bus_trial.head()

#######################
##
##  
##
#######################


clean_dict = []
for zip_code in demo.postal_code:
    row_dict = {}
    zip_code_df = bus_trial.loc[bus_trial['postal_code'] == zip_code]
    row_dict['postal_code'] = zip_code
    row_dict['num_business'] = zip_code_df.shape[0]
    row_dict['num_unique_business'] = len(zip_code_df.new_categories.value_counts()>0)
    clean_dict.append(row_dict)

clean_df = pd.DataFrame(clean_dict)



#inner join 
clean_df2 = pd.merge(clean_df,demo, on='postal_code', how='inner')

clean_df2['num_bus_per_cap']=clean_df2.num_business/clean_df2.population
clean_df2['num_uni_bus_per_cap']=clean_df2.num_unique_business/clean_df2.population

del clean_df2['Unnamed: 0']
clean_df2['country']='United States' #For cartodb
clean_df2.to_csv("ny_bus_explo.csv")

clean_df2.head()

#######################
##
##  
##
#######################

data_ana = []
for zip_code in demo.postal_code:
    row_dict = {}
    zip_code_df = bus_trial.loc[bus_trial['postal_code'] == zip_code]
    row_dict['postal_code'] = zip_code
    row_dict['Restaurants'] = len(zip_code_df[zip_code_df['new_categories'] == "Restaurants"])
    row_dict['Food'] = len(zip_code_df[zip_code_df['new_categories'] == "Food"])
    row_dict['Shopping'] = len(zip_code_df[zip_code_df['new_categories'] == "Shopping"])
    row_dict['Beauty and Spas'] = len(zip_code_df[zip_code_df['new_categories'] == "Beauty and Spas"])
    row_dict['Health and Medical'] = len(zip_code_df[zip_code_df['new_categories'] == "Health and Medical"])
    row_dict['Nightlife'] = len(zip_code_df[zip_code_df['new_categories'] == "Nightlife"])
    row_dict['Local Services'] = len(zip_code_df[zip_code_df['new_categories'] == "Local Services"])
    row_dict['Home Services'] = len(zip_code_df[zip_code_df['new_categories'] == "Home Services"])
    row_dict['Automotive'] = len(zip_code_df[zip_code_df['new_categories'] == "Automotive"])
    row_dict['Active Life'] = len(zip_code_df[zip_code_df['new_categories'] == "Active Life"])
    row_dict['Hotels & Travel'] = len(zip_code_df[zip_code_df['new_categories'] == "Hotels & Travel"])
    row_dict['Pets'] = len(zip_code_df[zip_code_df['new_categories'] == "Pets"])
    row_dict['Event Planning & Services'] = len(zip_code_df[zip_code_df['new_categories'] == "Event Planning & Services"])
    row_dict['Professional Services'] = len(zip_code_df[zip_code_df['new_categories'] == "Professional Services"])
    row_dict['Arts & Entertainment'] = len(zip_code_df[zip_code_df['new_categories'] == "Arts & Entertainment"])
    row_dict['Education'] = len(zip_code_df[zip_code_df['new_categories'] == "Education"])
    row_dict['Real Estate'] = len(zip_code_df[zip_code_df['new_categories'] == "Real Estate"])
    row_dict['Financial Services'] = len(zip_code_df[zip_code_df['new_categories'] == "Financial Services"])
    row_dict['Public Services & Government'] = len(zip_code_df[zip_code_df['new_categories'] == "Public Services & Government"])
    row_dict['Religious Organizations'] = len(zip_code_df[zip_code_df['new_categories'] == "Religious Organizations"])
    row_dict['Mass Media'] = len(zip_code_df[zip_code_df['new_categories'] == "Mass Media"])
    data_ana.append(row_dict)

impact_df = pd.DataFrame(data_ana)
impact_df2 = pd.merge(impact_df,demo, on='postal_code', how='inner')
impact_df2['num_household']=impact_df2.population/impact_df2.household_size

import matplotlib.pyplot
import seaborn as sn
%matplotlib inline
