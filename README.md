# foodComputerV2
## Website (with data displays)
nielsnovotny.com
## Paper (work in progress)
### Using the Normalized Difference Vegetation Index to adjust temperatures to optimize plant growth
#### Introduction
Climate change is making farming increasingly difficult in the wild where unpredictable weather and rising temperatures are detrimental to crops[1]. A solution to this is growing plants in controlled environments, Controlled Environment Agriculture (CEA) is the use of a computer-controlled environment to create the most optimal environment for a plant to grow in [3]. The widespread use of CEA is limited due to its large demand for energy [5]. Much of this energy is spent heating and cooling the environment [5]. Because so much money is being spent on heating and cooling the environment, having a temperature that allows for maximum plant productivity while being the closest to the resting temperature of the greenhouse would benefit farmers.

This paper will examine the use of the Normalized Difference Vegetation Index (NDVI) to optimize temperature in a controlled growing environment.
#### Background
The NDVI uses the near infrared (NIR) spectrum and the red spectrum to determine how efficiently the plant is using light [6]. Chlorophyll (used in photosynthesis) absorbs most red light and reflects most NIR light [8]. So by comparing the amount of red light to NIR light we are able to determine how much light the plant is reflecting, illustrated by the NDVI equation NDVI = (NIR-R)/(NIR + R)[2]. High amounts of reflected light are suboptimal for the plant as the plant absorbs less energy[6].

As plants become more stressed they reflect more light than normal [6, 9]; this paper will examine if the stress from varying temperatures is high enough to 1. affect the NDVI levels and 2. adjust the temperature according to the NDVI.
#### Procedure
Three controlled growth environments are set up. One controlled growth environment will start at 85 degrees fahrenheit (the temperature above the control). The other controlled growth environment started at a 70 degrees fahrenheit (the  temperature below the control). And the control environment stayed at 77 degrees fahrenheit. The temperature of the low and high temperature environments gravitated toward the temperature of the environment with the healthiest plants (plant  health is determined based off of the NDVI which will come in a range from +1.0 (good) to -1.0 (bad)). The temperature was adjusted according to a PID formula, Tn+1​=Tn​+Kp​en​+Ki​∑i=1n​ei​Δt+Kd​Δten​−en−1​, the temperature was adjusted every two days.
#### Materials / Methods
A raspberry pi was used to drive the environments. To operate the lights a relay was used. To measure temperature and humidity a DHT11 was used. To take soil moisture the (insert part number) was used. To water the plants a simple pump was connected to a water reservoir of tap water. To increase heat a heater with a fan attached was used and to lower the temperature an exhaust fan was used. To increase humidity a mister was connected with a high pressure pump. These sensors and actuators kept the temperature according to the experiment, the humidity from 50%-60%, and the soil moisture between 15% and 50%. In order to measure the NDVI, two Raspberry Pi cameras were used in each environment; one with a NIR filter and one without a filter. Then, the cameras determined the NDVI value by rescaling each pixel in the picture (done by Jon Williams, github page). Finally, the areas of the image containing plants were determined through NDVI thresholding and the NDVI for each plant in the environment was averaged to get the score for the environment.
#### Results
In the first week, each lettuce (saplings at this point) measured 0.7 on the NDVI. This is because the plants have just germinated and have yet to adjust to their temperature and show any signs of stress.
#### Bibliography
1 .Mestre-Sanchís, Fernando, and María Luisa Feijóo-Bello. "Climate change and its marginalizing effect on agriculture." Ecological Economics, vol. 68, no. 3, 2009, pp. 896-904. https://doi.org/10.1016/j.ecolecon.2008.07.015.
Outlines problems faced by farmers due to climate change, especially effects of rain. This can support my introduction as it can explain the need for controlled environment agriculture.
2 .Ghazal, Sumaira, et al. "Computer vision in smart agriculture and precision farming: Techniques and applications." Artificial Intelligence in Agriculture, vol. 13, 2024, pp. 64-83. https://doi.org/10.1016/j.aiia.2024.06.004.
Outlines process for getting crop health indicators that are visible to cameras. This article provides formulas for calculating NDVI. It outlines the different spectrums required for different indexes, the process of image stitching, image analysis, and creating a solution.
3. Tsitsimpelis, Ioannis, et al. "Development of a grow-cell test facility for research into sustainable controlled-environment agriculture." Biosystems Engineering, vol. 150, 2016, pp. 40-53. https://doi.org/10.1016/j.biosystemseng.2016.07.008.
Outlines controlled environment agriculture. It examines different layouts and configurations to maximize space utilization and it examines the emissions of different light spectrums from grow lights and their placement.
4. Carotti, Laura, et al. "Plant Factories Are Heating Up: Hunting for the Best Combination of Light Intensity, Air Temperature and Root-Zone Temperature in Lettuce Production." Frontiers in Plant Science, vol. 11, 2021. https://doi.org/10.3389/fpls.2020.592171.
Examines the effects of temperature variation in the roots and in the surrounding air on the growth and health od lettuce plants. This doesn’t examine its effect on NDVI but it can be used as a template as to how the plant should generally respond.
5. Williams, Jon. “Biomaker/22_DIY_plant_multispectral_imager: An Open-Source Arduino-Based Multispectral Camera.” GitHub, Biomaker Challenge Organisers, github.com/Biomaker/22_DIY_plant_multispectral_imager. Accessed 5 May 2025. 
Uses low cost cameras with a filter to determine the NDVI. This is useful as I will use this framework to measure the NDVI of my plants.
6.Nemali, Krishna. Detecting Crop Light Use from Normalized Difference Vegetation Index (NDVI). Purdue Extension, Feb. 2018. HO-282-W. https://www.extension.purdue.edu/extmedia/HO/HO-282-W%20.pdf.
Examines the use of NDVI to detect the usage of light by plants then adjust light intensity to save money. This is very useful as it is very similar to my project, except it examines light usage instead of temperature.
7.Lorditch, Emilie. “Ask the Expert: Could Controlled Environment Agriculture Be the Future of Farming and Solve Food Insecurity?” MSUToday, Michigan State University, 2 June 2023, msutoday.msu.edu/news/2023/ask-the-expert-could-controlled-environment-agriculture-be-the-future-of-farming?collection=79022467-cc5d-4b0d-9d69-8f773df52178. 
Outlines problems faced by farmers using CEA. Especially emphasises that energy is lost heating and cooling greenhouses/artificial environments.
8. Aparicio, N., D. Villegas, J. Casadesus, J.L. Araus, and C. Royo. 2000. Spectral vegetation indices as nondestructive tools for determining durum wheat yield. Agron. J. 92: 83-91.
Examines different remote sensing technologies to determine the health of wheat crops. It examines NDVI in specific.
9. Ehleringer, J.R. and O. Bjorkman. 1978. Pubescence and leaf spectral characteristics in a desert shrub, Encelia farinosa. Oecologia. 36: 151-162.
Discusses the effects of stress on light usage, which directly affects NDVI.


