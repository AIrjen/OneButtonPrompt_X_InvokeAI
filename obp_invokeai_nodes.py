from invokeai.invocation_api import (
    BaseInvocation,
    BaseInvocationOutput,
    InvocationContext,
    invocation,
    invocation_output,
    InputField,
    UIComponent,
    StringOutput,
    OutputField
)
from typing import Literal
from datetime import datetime
import os
import platform
import uuid

from .build_dynamic_prompt import *
from .csv_reader import *
from .one_button_presets import OneButtonPresets

OBPresets = OneButtonPresets()
allpresets = [OBPresets.RANDOM_PRESET_OBP] + list(OBPresets.opb_presets.keys())

artists = Literal["all", "all (wild)", "none", "popular", "greg mode", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", "cinema", 	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"gore",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"nudity",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
artifyartists = Literal["all", "all (wild)", "popular", "greg mode", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", "cinema", 	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"gore",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"nudity",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
imagetypes = Literal["all", "all - force multiple", "all - anime", "none", "photograph", "octane render","digital art","concept art", "painting", "portrait", "anime", "only other types", "only templates mode", "dynamic templates mode", "art blaster mode", "quality vomit mode", "color cannon mode", "unique art mode", "massive madness mode", "photo fantasy mode", "subject only mode", "fixed styles mode", "the tokinator"]
subjects = Literal["all", "object", "animal", "humanoid", "landscape", "concept"]
genders = Literal["all", "male", "female"]
emojis = Literal[False, True]

models = Literal["SD1.5", "SDXL", "Stable Cascade", "Anime Model"]
prompt_enhancers = Literal["none", "superprompt-v1"]
subjects = ["------ all"]
subjectsubtypesobject = ["all"]
subjectsubtypeshumanoid = ["all"]
subjectsubtypesconcept = ["all"]
#subjectsubtypesobject = ["all", "generic objects", "vehicles", "food", "buildings", "space", "flora"]
#subjectsubtypeshumanoid = ["all", "generic humans", "generic human relations", "celebrities e.a.", "fictional characters", "humanoids", "based on job or title", "based on first name"]
#subjectsubtypesconcept = ["all", "event", "the X of Y concepts", "lines from poems", "lines from songs"]

amountofflufflist = Literal["none", "dynamic", "short", "medium", "long"]
fluff_reverse_polarity = Literal[False,True]

artifymodeslist = Literal["standard", "remix", "super remix turbo"]
artifyamountofartistslist = Literal["random", "0", "1", "2", "3", "4", "5"]

superprompterstyleslist = ['all']
superprompterstyleslist += csv_to_list("superprompter_styles")


# Load up stuff for personal artists list, if any
# find all artist files starting with personal_artits in userfiles
script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
userfilesfolder = os.path.join(script_dir, "./userfiles/" )
for filename in os.listdir(userfilesfolder):
    if(filename.endswith(".csv") and filename.startswith("personal_artists") and filename != "personal_artists_sample.csv"):
        name = os.path.splitext(filename)[0]
        name = name.replace("_"," ",-1).lower()
        # directly insert into the artists list
        artists.insert(2, name)

# on startup, check if we have a config file, or else create it
config = load_config_csv()  


# load subjects stuff from config
generatevehicle = True
generateobject = True
generatefood = True
generatebuilding = True
generatespace = True
generateflora = True

generateanimal = True
generatebird = True
generatecat = True
generatedog = True
generateinsect = True
generatepokemon = True
generatemarinelife = True

generatemanwoman = True
generatemanwomanrelation = True
generatemanwomanmultiple = True
generatefictionalcharacter = True
generatenonfictionalcharacter = True
generatehumanoids = True
generatejob = True
generatefirstnames = True

generatelandscape = True
generatelocation = True
generatelocationfantasy = True
generatelocationscifi = True
generatelocationvideogame = True
generatelocationbiome = True
generatelocationcity = True

generateevent = True
generateconcepts = True
generatepoemline = True
generatesongline = True
generatecardname = True
generateepisodetitle = True
generateconceptmixer = True


for item in config:
        # objects
        if item[0] == 'subject_vehicle' and item[1] != 'on':
            generatevehicle = False
        if item[0] == 'subject_object' and item[1] != 'on':
            generateobject = False
        if item[0] == 'subject_food' and item[1] != 'on':
            generatefood = False
        if item[0] == 'subject_building' and item[1] != 'on':
            generatebuilding = False
        if item[0] == 'subject_space' and item[1] != 'on':
            generatespace = False
        if item[0] == 'subject_flora' and item[1] != 'on':
            generateflora = False
        # animals
        if item[0] == 'subject_animal' and item[1] != 'on':
            generateanimal = False
        if item[0] == 'subject_bird' and item[1] != 'on':
            generatebird = False
        if item[0] == 'subject_cat' and item[1] != 'on':
            generatecat = False
        if item[0] == 'subject_dog' and item[1] != 'on':
            generatedog = False
        if item[0] == 'subject_insect' and item[1] != 'on':
            generateinsect = False
        if item[0] == 'subject_pokemon' and item[1] != 'on':
            generatepokemon = False
        if item[0] == 'subject_marinelife' and item[1] != 'on':
            generatemarinelife = False
        # humanoids
        if item[0] == 'subject_manwoman' and item[1] != 'on':
            generatemanwoman = False
        if item[0] == 'subject_manwomanrelation' and item[1] != 'on':
            generatemanwomanrelation = False
        if item[0] == 'subject_manwomanmultiple' and item[1] != 'on':
            generatemanwomanmultiple = False
        if item[0] == 'subject_fictional' and item[1] != 'on':
            generatefictionalcharacter = False
        if item[0] == 'subject_nonfictional' and item[1] != 'on':
            generatenonfictionalcharacter = False
        if item[0] == 'subject_humanoid' and item[1] != 'on':
            generatehumanoids = False
        if item[0] == 'subject_job' and item[1] != 'on':
            generatejob = False
        if item[0] == 'subject_firstnames' and item[1] != 'on':
            generatefirstnames = False
        # landscape
        if item[0] == 'subject_location' and item[1] != 'on':
            generatelocation = False
        if item[0] == 'subject_location_fantasy' and item[1] != 'on':
            generatelocationfantasy = False
        if item[0] == 'subject_location_scifi' and item[1] != 'on':
            generatelocationscifi = False
        if item[0] == 'subject_location_videogame' and item[1] != 'on':
            generatelocationvideogame = False
        if item[0] == 'subject_location_biome' and item[1] != 'on':
            generatelocationbiome = False
        if item[0] == 'subject_location_city' and item[1] != 'on':
            generatelocationcity = False
        # concept
        if item[0] == 'subject_event' and item[1] != 'on':
            generateevent = False
        if item[0] == 'subject_concept' and item[1] != 'on':
            generateconcepts = False
        if item[0] == 'subject_poemline' and item[1] != 'on':
            generatepoemline = False
        if item[0] == 'subject_songline' and item[1] != 'on':
            generatesongline = False
        if item[0] == 'subject_cardname' and item[1] != 'on':
            generatecardname = False
        if item[0] == 'subject_episodetitle' and item[1] != 'on':
            generateepisodetitle = False
        if item[0] == 'subject_conceptmixer' and item[1] != 'on':
            generateconceptmixer = False

# build up all subjects we can choose based on the loaded config file
if(generatevehicle or generateobject or generatefood or generatebuilding or generatespace or generateflora):
    subjects.append("--- object - all")
    if(generateobject):
          subjects.append("object - generic")
    if(generatevehicle):
          subjects.append("object - vehicle")
    if(generatefood):
          subjects.append("object - food")
    if(generatebuilding):
          subjects.append("object - building")
    if(generatespace):
          subjects.append("object - space")
    if(generateflora):
          subjects.append("object - flora")
          
if(generateanimal or generatebird or generatecat or generatedog or generateinsect or generatepokemon or generatemarinelife):
    subjects.append("--- animal - all")
    if(generateanimal):
        subjects.append("animal - generic")
    if(generatebird):
        subjects.append("animal - bird")
    if(generatecat):
        subjects.append("animal - cat")
    if(generatedog):
        subjects.append("animal - dog")
    if(generateinsect):
        subjects.append("animal - insect")
    if(generatemarinelife):
        subjects.append("animal - marine life")
    if(generatepokemon):
        subjects.append("animal - pokémon")

if(generatemanwoman or generatemanwomanrelation or generatefictionalcharacter or generatenonfictionalcharacter or generatehumanoids or generatejob or generatemanwomanmultiple):
    subjects.append("--- human - all")
    if(generatemanwoman):
        subjects.append("human - generic")
    if(generatemanwomanrelation):
        subjects.append("human - relations")
    if(generatenonfictionalcharacter):
        subjects.append("human - celebrity")
    if(generatefictionalcharacter):
        subjects.append("human - fictional")
    if(generatehumanoids):
        subjects.append("human - humanoids")
    if(generatejob):
        subjects.append("human - job/title")
    if(generatefirstnames):
        subjects.append("human - first name")
    if(generatemanwomanmultiple):
        subjects.append("human - multiple")

if(generatelandscape or generatelocation or generatelocationfantasy or generatelocationscifi or generatelocationvideogame or generatelocationbiome or generatelocationcity):
    subjects.append("--- landscape - all")
    if(generatelocation):
        subjects.append("landscape - generic")
    if(generatelocationfantasy):
        subjects.append("landscape - fantasy")
    if(generatelocationscifi):
        subjects.append("landscape - sci-fi")
    if(generatelocationvideogame):
        subjects.append("landscape - videogame")
    if(generatelocationbiome):
        subjects.append("landscape - biome")
    if(generatelocationcity):
        subjects.append("landscape - city")

if(generateevent or generateconcepts or generatepoemline or generatesongline or generatecardname or generateepisodetitle or generateconceptmixer):
    subjects.append("--- concept - all")
    if(generateevent):
        subjects.append("concept - event")
    if(generateconcepts):
        subjects.append("concept - the x of y")
    if(generatepoemline):
        subjects.append("concept - poem lines")
    if(generatesongline):
        subjects.append("concept - song lines")
    if(generatecardname):
        subjects.append("concept - card names")
    if(generateepisodetitle):
        subjects.append("concept - episode titles")
    if(generateconceptmixer):
        subjects.append("concept - mixer")


# do the same for the subtype subjects
# subjectsubtypesobject = ["all"]
# subjectsubtypeshumanoid = ["all"]
# subjectsubtypesconcept = ["all"]

# objects first
if(generateobject):
     subjectsubtypesobject.append("generic objects")
if(generatevehicle):
     subjectsubtypesobject.append("vehicles")
if(generatefood):
     subjectsubtypesobject.append("food")
if(generatebuilding):
     subjectsubtypesobject.append("buildings")
if(generatespace):
     subjectsubtypesobject.append("space")
if(generateflora):
     subjectsubtypesobject.append("flora")

# humanoids (should I review descriptions??)
if(generatemanwoman):
     subjectsubtypeshumanoid.append("generic humans")
if(generatemanwomanrelation):
     subjectsubtypeshumanoid.append("generic human relations")
if(generatenonfictionalcharacter):
     subjectsubtypeshumanoid.append("celebrities e.a.")
if(generatefictionalcharacter):
     subjectsubtypeshumanoid.append("fictional characters")
if(generatehumanoids):
     subjectsubtypeshumanoid.append("humanoids")
if(generatejob):
     subjectsubtypeshumanoid.append("based on job or title")
if(generatefirstnames):
     subjectsubtypeshumanoid.append("based on first name")
if(generatemanwomanmultiple):
     subjectsubtypeshumanoid.append("multiple humans")

# concepts
if(generateevent):
     subjectsubtypesconcept.append("event")
if(generateconcepts):
     subjectsubtypesconcept.append("the X of Y concepts")
if(generatepoemline):
     subjectsubtypesconcept.append("lines from poems")
if(generatesongline):
     subjectsubtypesconcept.append("lines from songs")
if(generatecardname):
     subjectsubtypesconcept.append("names from card based games")
if(generateepisodetitle):
     subjectsubtypesconcept.append("episode titles from tv shows")
if(generateconceptmixer):
     subjectsubtypesconcept.append("concept mixer")

# Lets just smash this into lits for invoke stuff
subjects_lit = Literal[tuple(subjects)]
presets_lit = Literal[tuple(allpresets)]
superprompterstyleslist_lit = Literal[tuple(superprompterstyleslist)]


# main OBP node
@invocation_output("OBP_output")
class OBPOutput(BaseInvocationOutput):
    one_button_prompt: str = OutputField(description="The positive prompt that is generated by the One Button Prompt node.")

@invocation(
    "OneButtonPrompt",
    title="One Button Prompt",
    tags=["prompt", "random","OBP", "OneButtonPrompt"],
    category="prompt",
    version="1.0.0",
    use_cache=False,
)
class OneButtonPrompt(BaseInvocation):
    """Main One Button Prompt node, generates a random prompt based on several set parameters."""
    insanity_level: int = InputField(default=5, description="Randomness of the generated prompt.")
    artist: artists = InputField(default="all", description="Type of artists to add to the prompt.")
    imagetype: imagetypes = InputField(default="all", description="Type of image, or mode of prompt generation.")
    imagemodechance: int = InputField(default=20, description="X in 100 chance to pick a random image type mode.")
    subject: subjects_lit = InputField(default="------ all", description="Type of subject to generate.")
    humanoids_gender: genders = InputField(default="all", description="Type of gender to apply to humanoid subjects.")
    override_subject: str = InputField(default="", description="Override the main subject of the generation.")
    override_outfit: str = InputField(default="", description="Apply this outfit to the generation")
    base_model: models = InputField(default="SDXL", description="Type of model to generate prompt for. Affects prompt generation.")
    prompt_enhancer: prompt_enhancers  = InputField(default="none", description="Apply this prompt enhancer, like superprompter.")

    
    #custom_subject: str = InputField(
   #     default="", description="Subject Override", ui_component=UIComponent.Textarea
    #)
    
    def invoke(self, context: InvocationContext) -> OBPOutput:
        prompt = build_dynamic_prompt(insanitylevel=self.insanity_level,
                                      artists=self.artist,
                                      imagetype=self.imagetype,
                                      imagemodechance=self.imagemodechance,
                                      forcesubject=self.subject,
                                      gender=self.humanoids_gender,
                                      givensubject=self.override_subject,
                                      overrideoutfit=self.override_outfit,
                                      base_model=self.base_model,
                                      prompt_enhancer=self.prompt_enhancer
                                      )
        
        return OBPOutput(one_button_prompt=prompt)


#Create Prompt Variant node
@invocation_output("CreatePromptVariant_output")
class CreatePromptVariantOutput(BaseInvocationOutput):
    positive_prompt_variant: str = OutputField(description="The variation of the positive prompt.")

@invocation(
    "CreatePromptVariant",
    title="Create Prompt Variant",
    tags=["prompt", "variant","OBP", "OneButtonPrompt"],
    category="prompt",
    version="1.0.0",
    use_cache=False,
)
class CreatePromptVariant(BaseInvocation):
    """Creates a slight variation in the prompt that was inserted."""
    prompt_input: str = InputField(
         default="A old painting of a fluffy cat wearing a sleek hat", description="Create variant of this prompt.", ui_component=UIComponent.Textarea
    )
    insanity_level: int = InputField(default=5, description="Randomness of the generated prompt.")
    

    
    def invoke(self, context: InvocationContext) -> CreatePromptVariantOutput:
        prompt = createpromptvariant(insanitylevel=self.insanity_level,
                                     prompt=self.prompt_input
                                      
                                      )
        print("This is the prompt variant: " + prompt)
        return CreatePromptVariantOutput(positive_prompt_variant=prompt)


# One Button Preset Node
@invocation_output("OBPreset_output")
class OBPresetOutput(BaseInvocationOutput):
    one_button_prompt: str = OutputField(description="The positive prompt that is generated by the One Button Preset node.")

@invocation(
    "OneButtonPreset",
    title="One Button Preset",
    tags=["prompt", "preset","OBP", "OneButtonPrompt"],
    category="prompt",
    version="1.0.0",
    use_cache=False,
)
class OneButtonPreset(BaseInvocation):
    """Same as the main One Button Prompt node, but works on all settings being preset."""
    OneButtonPreset: presets_lit = InputField(default="Standard", description="Preset to use for prompt generation.")
    base_model: models = InputField(default="SDXL", description="Type of model to generate prompt for. Affects prompt generation.")
    prompt_enhancer: prompt_enhancers  = InputField(default="none", description="Apply this prompt enhancer.")
    preset_prefix: str = InputField(
         default="", description="Add this text to the front of the generated prompt.", ui_component=UIComponent.Textarea
    )
    preset_suffix: str = InputField(
         default="", description="Add this text to the back of the generated prompt.", ui_component=UIComponent.Textarea
    )

    
    def invoke(self, context: InvocationContext) -> OBPresetOutput:
        if(self.OneButtonPreset == OBPresets.RANDOM_PRESET_OBP):
            selected_opb_preset = OBPresets.get_obp_preset("Standard")
        else:
            selected_opb_preset = OBPresets.get_obp_preset(self.OneButtonPreset)
        
        insanitylevel=selected_opb_preset["insanitylevel"]
        subject=selected_opb_preset["subject"]
        artist=selected_opb_preset["artist"]
        chosensubjectsubtypeobject=selected_opb_preset["chosensubjectsubtypeobject"]
        chosensubjectsubtypehumanoid=selected_opb_preset["chosensubjectsubtypehumanoid"]
        chosensubjectsubtypeconcept=selected_opb_preset["chosensubjectsubtypeconcept"]
        chosengender=selected_opb_preset["chosengender"]
        imagetype=selected_opb_preset["imagetype"]
        imagemodechance=selected_opb_preset["imagemodechance"]
        givensubject=selected_opb_preset["givensubject"]
        smartsubject=selected_opb_preset["smartsubject"]
        givenoutfit=selected_opb_preset["givenoutfit"]
        prefixprompt=selected_opb_preset["prefixprompt"]
        suffixprompt=selected_opb_preset["suffixprompt"]
        giventypeofimage=selected_opb_preset["giventypeofimage"]
        antistring=selected_opb_preset["antistring"]
        
        prompt = build_dynamic_prompt(insanitylevel=insanitylevel,
                                               forcesubject=subject,
                                               artists=artist,
                                               subtypeobject=chosensubjectsubtypeobject,
                                               subtypehumanoid=chosensubjectsubtypehumanoid,
                                               subtypeconcept=chosensubjectsubtypeconcept,
                                               gender=chosengender,
                                               imagetype=imagetype,
                                               imagemodechance=imagemodechance,
                                               givensubject=givensubject,
                                               smartsubject=smartsubject,
                                               overrideoutfit=givenoutfit,
                                               prefixprompt=prefixprompt,
                                               suffixprompt=suffixprompt,
                                               giventypeofimage=giventypeofimage,
                                               antivalues=antistring,
                                               advancedprompting=False,
                                               hardturnoffemojis=True,
                                               base_model=self.base_model,
                                               OBP_preset=self.OneButtonPreset,
                                               prompt_enhancer=self.prompt_enhancer,
                                               preset_prefix=self.preset_prefix,
                                               preset_suffix=self.preset_suffix,
                                               )
        
        return OBPresetOutput(one_button_prompt=prompt)

@invocation_output("SavePromptToFile_output")
class SavePromptToFileOutput(BaseInvocationOutput):
    positive_prompt: str = OutputField(description="The positive prompt that was inputted.")
    negative_prompt: str = OutputField(description="The negative prompt that was inputted.")
    
@invocation(
    "SavePromptToFile",
    title="Save Prompt To File",
    tags=["prompt", "file","save", "text", "OBP", "OneButtonPrompt"],
    category="prompt",
    version="1.0.0",
    use_cache=False,
)
class SavePromptToFile(BaseInvocation):
    """Saves the input prompts to a file in \outputs\OBP_prompt_storage\ folder"""
    positive_prompt: str = InputField(
         default="A painting of a fluffy cat wearing a sleek hat", description="The positive prompt to save to the file.", ui_component=UIComponent.Textarea
    )
    negative_prompt: str = InputField(
         default="", description="The negative prompt to save to the file.", ui_component=UIComponent.Textarea
    )
    filename_prefix: str = InputField(
         default="", description="Prefix that is added the the file."
    )
       

    
    def invoke(self, context: InvocationContext) -> SavePromptToFileOutput:
        # Some stuff for the prefix
        
        # turns out there is some hardcoded stuff on saveimage we have to kind of repeat here
        # Find the %date:yyyy-M-d% pattern using regular expression
        pattern = r'%date:([^\%]+)%'
        match = re.search(pattern, self.filename_prefix)

        if match:
            # Extract the date format from the match
            date_format = match.group(1)

            # Get the current date
            current_date = datetime.now()

            # convert the ComfyUI standard into Python standard format.
            # What a crazy way of doing this
            # first lol, I got to make sure it doesn't overlap things
            date_format = date_format.replace('M', 'X')
            date_format = date_format.replace('m', 'Z')
            
            # This is so bad

            # lets make it even worse, it work differently on windows than in Linux
            if(platform.system() == 'Windows'):

                date_format = date_format.replace('yyyy', '%Y')
                date_format = date_format.replace('yy', '%#y')
                date_format = date_format.replace('X', '%#m')
                date_format = date_format.replace('d', '%#d')
                date_format = date_format.replace('h', '%#H')
                date_format = date_format.replace('Z', '%#M')
                date_format = date_format.replace('s', '%#S')
            else:
                date_format = date_format.replace('yyyy', '%Y')
                date_format = date_format.replace('yy', '%-y')
                date_format = date_format.replace('X', '%-m')
                date_format = date_format.replace('d', '%-d')
                date_format = date_format.replace('h', '%-H')
                date_format = date_format.replace('Z', '%-M')
                date_format = date_format.replace('s', '%-S')


            # Format the date using the extracted format
            formatted_date = current_date.strftime(date_format)

            # Replace the matched pattern with the formatted date
            filename_prefix_compl = re.sub(pattern, formatted_date, self.filename_prefix)
        else:
            filename_prefix_compl = self.filename_prefix   

           

        # make the filename, from from a to the first comma
        # find the index of the first comma after "of a" or end of the prompt
        if(self.positive_prompt.find("of a ") != -1):
            start_index = self.positive_prompt.find("of a ") + len("of a ")
            end_index = self.positive_prompt.find(",", start_index)
            if(end_index == -1):
                end_index=len(self.positive_prompt)
        else:
            start_index = 0
            end_index = 128
  
        # extract the desired substring using slicing
        filename = self.positive_prompt[start_index:end_index]

        # cleanup some unsafe things in the filename
        filename = filename.replace("\"", "")
        filename = filename.replace("[", "")
        filename = filename.replace("|", "")
        filename = filename.replace("]", "")
        filename = filename.replace("<", "")
        filename = filename.replace(">", "")
        filename = filename.replace(":", "_")
        filename = filename.replace(".", "")
        filename = re.sub(r'[0-9]+', '', filename)

        safe_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")

        # Use regular expression to filter out any characters not in the whitelist
        filename = re.sub(r"[^{}]+".format(re.escape(''.join(safe_characters))), '', filename)
        

        if(filename==""):
            filename = str(uuid.uuid4())
        
        if(filename_prefix_compl == ""):
        # create a datetime object for the current date and time
        # if there is no prefix
            now = datetime.now()
            filenamecomplete = now.strftime("%Y%m%d%H%M%S") + "_" + filename.replace(" ", "_").strip() + ".txt"
        
        else:
            filenamecomplete = filename.replace(" ", "_").strip() + ".txt"
    
        full_output_folder = ".\\outputs\\OBP_prompt_storage\\"
        # Create the directory if it doesn't exist
        os.makedirs(full_output_folder, exist_ok=True)

        directoryandfilename = os.path.abspath(os.path.join(full_output_folder, filenamecomplete))
        

        with open(directoryandfilename, 'w', encoding="utf-8") as file:
            file.write("prompt: " + self.positive_prompt + "\n")
            
            #if(len(self.prompt_g) > 0):
            #    file.write("prompt_g: " + self.prompt_g + "\n")
            #if(len(self.prompt_l) > 0):
            #    file.write("prompt_l: " + self.prompt_l + "\n")
            
            file.write("negative prompt: " + self.negative_prompt + "\n")



        return SavePromptToFileOutput(positive_prompt=self.positive_prompt,
                                      negative_prompt=self.negative_prompt)
    

#Auto negative prompt node
@invocation_output("AutoNegativePrompt_output")
class AutoNegativePromptOutput(BaseInvocationOutput):
    negative_prompt: str = OutputField(description="The generated negative prompt.")

@invocation(
    "AutoNegativePrompt",
    title="Auto Negative Prompt",
    tags=["prompt", "Negative","OBP", "OneButtonPrompt"],
    category="prompt",
    version="1.0.0",
    use_cache=False,
)
class AutoNegativePrompt(BaseInvocation):
    """Generates a negative prompt based on the positive prompt."""
    positive_prompt: str = InputField(
         default="", description="Creates a negative prompt based on the positive prompt.", ui_component=UIComponent.Textarea
    )
    base_negative: str = InputField(
         default="text, watermark", description="Always add these words to the negative prompt.", ui_component=UIComponent.Textarea
    )
    enhance_negative: int = InputField(default=0, description="0 = no, 1 = yes, adds a standard basic set of words to the negative prompt.")
    insanity_level: int = InputField(default=0, description="Randomness of the generated negative prompt. 0 keeps all.")
    base_model: models = InputField(default="SDXL", description="Type of model to generate prompt for. Affects prompt generation.")
    

    
    def invoke(self, context: InvocationContext) -> AutoNegativePromptOutput:
        negative_prompt = build_dynamic_negative(insanitylevel=self.insanity_level,
                                                positive_prompt=self.positive_prompt,
                                                enhance=self.enhance_negative,
                                                existing_negative_prompt=self.base_negative,
                                                base_model=self.base_model
                                                )
        print("This is the generated negative prompt: " + negative_prompt)
        return AutoNegativePromptOutput(negative_prompt=negative_prompt)
    
#One Button Artify node
@invocation_output("OneButtonArtify_output")
class OneButtonArtifyOutput(BaseInvocationOutput):
    artified_prompt: str = OutputField(description="The prompt that has been artified.")

@invocation(
    "OneButtonArtify",
    title="One Button Artify",
    tags=["prompt", "Artify","OBP", "OneButtonPrompt"],
    category="prompt",
    version="1.0.0",
    use_cache=False,
)
class OneButtonArtify(BaseInvocation):
    """Adds artist names and descriptions to the prompt."""
    positive_prompt: str = InputField(
         default="a corgi wearing sunglasses", description="The prompt to be artified.", ui_component=UIComponent.Textarea
    )
    artist: artifyartists = InputField(default="all", description="Type of artists to artify your prompt with.")
    amount_of_artists: int = InputField(default=1, description="Amount of artists to artify your prompt with.")
    artist: artifyartists = InputField(default="all", description="Type of artists to artify your prompt with.")
    artify_mode: artifymodeslist = InputField(default="standard", description="Different types artify modes.")
    
    
    def invoke(self, context: InvocationContext) -> OneButtonArtifyOutput:
        prompt = artify_prompt(                 prompt=self.positive_prompt,
                                                artists=self.artist,
                                                amountofartists=self.amount_of_artists,
                                                mode=self.artify_mode
                                                )
        print("This is the artified prompt: " + prompt)
        return OneButtonArtifyOutput(artified_prompt=prompt)
    
#One Button Flufferize node
@invocation_output("OneButtonFlufferize_output")
class OneButtonFlufferizeOutput(BaseInvocationOutput):
    fluffed_prompt: str = OutputField(description="This is the fully fluffed prompt.")

@invocation(
    "OneButtonFlufferize",
    title="One Button Flufferize",
    tags=["prompt", "Flufferize","OBP", "OneButtonPrompt"],
    category="prompt",
    version="1.0.0",
    use_cache=False,
)
class OneButtonFlufferize(BaseInvocation):
    """Adds quality enhancing words to the prompt."""
    positive_prompt: str = InputField(
         default="a still photo of a banana", description="The prompt to be fluffed.", ui_component=UIComponent.Textarea
    )
    amount_of_fluff: amountofflufflist = InputField(default="dynamic", description="Amount of fluff to add to the prompt.")
    reverse_polarity: bool = InputField(default=False, description="REVERSE THE POLARITY ON YOUR OWN RISK.")
    
    
    def invoke(self, context: InvocationContext) -> OneButtonFlufferizeOutput:
        prompt = flufferizer(                 prompt=self.positive_prompt,
                                                amountoffluff=self.amount_of_fluff,
                                                reverse_polarity=self.reverse_polarity
                                                )
        print("This is the fluffed prompt: " + prompt)
        return OneButtonFlufferizeOutput(fluffed_prompt=prompt)
    
#One Button Superprompt node
@invocation_output("OneButtonSuperprompt_output")
class OneButtonSuperpromptOutput(BaseInvocationOutput):
    super_prompt: str = OutputField(description="This is the super prompted prompt.")

@invocation(
    "OneButtonSuperprompt",
    title="One Button Superprompt",
    tags=["prompt", "Superprompt","OBP", "OneButtonPrompt"],
    category="prompt",
    version="1.0.0",
    use_cache=False,
)
class OneButtonSuperprompt(BaseInvocation):
    """Uses the Superprompt model to generate a prompt."""
    positive_prompt: str = InputField(
         default="strawberry", description="The prompt to be fed into the superprompt model.", ui_component=UIComponent.Textarea
    )
    insanity_level: int = InputField(default=5, description="Randomness of the superprompt.")
    superpromptstyle: superprompterstyleslist_lit = InputField(default="all", description="Guide the superprompt in a certain direction.")
    
    
    def invoke(self, context: InvocationContext) -> OneButtonSuperpromptOutput:
        prompt = one_button_superprompt(        prompt=self.positive_prompt,
                                                insanitylevel=self.insanity_level,
                                                superpromptstyle=self.superpromptstyle
                                                )
        print("This is the super prompt: " + prompt)
        return OneButtonSuperpromptOutput(super_prompt=prompt)