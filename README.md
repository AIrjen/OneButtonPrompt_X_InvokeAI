![OneButtonPrompt](https://github.com/AIrjen/OneButtonPrompt_X_InvokeAI/blob/main/images/background.png "These images are auto generated, see all generated prompts below")


---
# One Button Prompt X InvokeAI

# Summary

One Button Prompt is a tool/script for Automatic1111/ComfyUI/RuinedFooocus for beginners who have problems writing a good prompt, or advanced users who want to get inspired.

This repository a standalone version that is build for InvokAI and has the community nodes for One Button Prompt. The main project can be found [here](https://github.com/AIrjen/OneButtonPrompt)

It generates an entire prompt from scratch. It is random, but controlled. You simply load up the script and press generate, and let it surprise you. Several nodes have been added over time, giving you some fun prompt things to play around with.

It is a full AI prompt generator for Stable Diffusion, Flux and others. Feel free to use it on your personal favorite models.

Any other AI tool you are using? Midjourney? Dalle? No problem, I got it working on [a website here](https://airjen.pythonanywhere.com/). Just copy the prompt to your clipboard with a click, and paste it in any image generator tool.


# Invoke AI Nodes

One Button Prompt --> The main prompt generator node, generates a randomized prompt based on several input parameters.

One Button Preset --> Same as the main prompt generator node, but has preconfigured settings stored you can choose.

Auto Negative Prompt --> Creates a fitting negative prompt for any positive prompt.

Save Prompt To File --> Saves postive and negative prompt into the output folder under /OBP_prompt_storage/

Create Prompt Variant --> Creates a variation of your positive prompt, replaces and changes words in context.

One Button Artify --> Adds artists and their descriptions around the given prompt.

One Button Flufferize --> Adds quality enhancing tokens to the prompt.

One Button Superprompt --> An implementation of the Superprompt model for prompt generation.


![OPBNodes](https://github.com/AIrjen/OneButtonPrompt_X_InvokeAI/blob/main/images/OBP_nodes_invokeai.png "The InvokeAI nodes.")


### Some details

Don't get overwhelmed by the options, they will become more clear once you use it more.

For first time users, play around with the set presets.

It will generate between 0 and 3 artists, and add those the prompt.

It can generate the following subjects, while building a prompt:

1. object - Can be a random object, a building ,a vehicle, some food or objects from space.  

2. animal - A random (fictional) animal. Has a chance to have human characteristics, such as clothing added.  

3. humanoid - A random humanoid, males, females, fantasy types, fictional and non-fictional characters. Can add clothing, features and a bunch of other things.  

4. landscape - A landscape or a landscape with a building.  

5. concept - Can be a concept, such as "the X of Y", or an historical event such as "The Trojan War".  It can also do a line from a poem or from a song.

It mixes techniques such as prompt switching and hybrids. 

This generator will generate a complete full prompt for you, based on randomness. You can increase the slider, to include more things to put into the prompt. 
Recommended is keeping it around 3-7. Use 10 at your own risk.

There are a lot of special things build in, based on various research. Just try it, and let it surprise you.

Suggestion is to leave the prompt field empty, anything here will be added at the end of the generated prompt.  
It doesn't add anything to the negative prompt field, so feel free to add your favorite negative prompts here.  

For each Batch you run, it will create a new prompt. For each batch size, it will reuse the same prompt.


# Installing in InvokeAI
InvokeAI suggest that to use a node, add the node to the nodes folder found in your InvokeAI install location.

The suggested method is to use `git clone` to clone the repository the node is found in. Use `https://github.com/airjen/OneButtonPrompt_X_InvokeAI`

# Prompts and examples
![00081-1764500323](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e975309c-78bc-468b-980e-2e5445cadfdd)
> video game concept art, 2d game art, concept art, landscape of a Kokiri Forest, it is Tribal, Sun in the sky, designed by Atey Ghailan, detailed, masterpiece, Deathpunk, 35mm, Polychromatic, digital art, contemporary fine detail, stunning, unique, fine detail, aesthetic

![00095-1877749527](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/c140be7b-0857-47de-8610-a91c091d3e83)
> small centered composition, product shot, plain background, wallpaper art, in the center is an image of an epic beautiful ("The Orb of Elegance":1.2) , foliage, at Golden hour, side lit, Colorless, warm light, dynamic dramatic atmosphere, background inspired, dynamic composition, ambient light, fine detail

![00088-1877749520](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/d060a48c-41c7-4364-9bdb-80126b170c87)
> colorful art by Norm Rapmund, Fatigued 25 y.o. Girl of [Rot|Music], Comic book art, dynamic, detailed, portrait art by Brian Sum, luxurious sharp focus, highly contrasted, sunny, complex artistic color composition, magnificent, dynamic cinematic color, cool colors, beautiful composition, complimentary colors, beautiful

![00011-4053395104](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6b99aa1b-a54c-4013-9060-a11cb3678c5c)
> Pill Bug, Moon in the night, Barbiecore, Side lighting, 50mm, designed by Ilya Kuvshinov, sci-fi

![00066-1877749498](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e5c9d081-7202-47c6-9195-69cc90c01bbb)
> photograph, buxom Girl, Appealing, dressed in headwear, the Girl has a Pink Angelic Halo, Wide view, Grim, Long exposure, Iphone X, F/5, dreamy, dream, dark, cozy, highly enhanced, intricate artistic color, beautiful elegant, confident, intricate detail

![00017-2787914262](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/d53e7aee-72c0-4b27-b8e6-6e08a4bb1b72)
Origami, Anime, Concept art of a Shinto Foliage, Average, it is in a Star Wars setting, Narnia in background, at Dusk, (realism art designed by Agnes Martin:1.0) , natural lighting, Pastel Colors, masterpiece

![00070-3423685499](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/851f39fd-6050-4682-a756-31965313c69a)
>  (by Carne Griffiths:1.2) , Cyborg "Through the lens of poetry, ordinary moments transform into extraordinary tales of the human experience.", nature and River stone background, Bathed in shadows, Monochrome, beautiful, boring, fauna, cool colors, magnificent, modified, radiant, magical composition

![00022-2065006526](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/8e814495-000a-42a2-b39d-6ecd55769c95)
> Suprematism, "Worgen Infiltrator", abstract, limited color palette, geometric forms, Suprematism

![00003-334769067](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/1a7a056f-3a5a-4be4-b756-5e74da472368)
> attractive, Seductive Female Valkyrie, Dark matter background, fairy tale, Abstract Art, feminine

# Thank you
This one is for Jonseed! Hope you enjoy it.