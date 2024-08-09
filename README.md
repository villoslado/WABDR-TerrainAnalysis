# WABDR-TerrainAnalysis 🏔️🚙

Have you ever wondered what the Washington Backcountry Discovery Route (WABDR) looks like from a data perspective? This project was initiated to provide a deeper understanding.

## Project Overview

As an avid backcountry adventurer and off-road enthusiast, I embarked on this project to analyze the WABDR using geographical data. The aim is to gain insights into the route's terrain and challenges.

## Key Areas of Analysis

The WABDR has been divided into six sections, each analyzed based on three critical factors:

1. 📐 **Slope**: Assessing the steepness of the terrain.
2. 🧭 **Aspect**: Determining the slope’s orientation, providing insights into factors like sun exposure and potential snowmelt.
3. 🏔️ **Terrain Ruggedness Index (TRI)**: Evaluating the roughness of the terrain; a higher TRI indicates more challenging conditions.

## Tools and Technologies

The analysis leverages the following technologies:

- Google Earth Engine for obtaining elevation data 🛰️
- Python for data processing 🐍
- Geospatial libraries to interpret the data 🗺️

## Purpose

This project is a fusion of my passion for off-roading and data analysis. The insights derived can be valuable for trip planning, understanding the difficulty of various sections, or simply exploring the terrain from a data-driven perspective. 🤓

## How to Use

To execute these scripts:

1. Start by running `bdr_data_downloader.py`. Please note that this process may take some time.
2. Once the data is downloaded, proceed to run `bdr_terrain_analyzer.py` to process the data and generate the results.

## 🚨 Important Considerations

While the analysis is thorough, there are some limitations to be aware of:

### 📏 Resolution Constraints
- The data has a resolution of approximately 30 meters per pixel, which may omit finer details of the terrain.

### 🗺️ Averaging Over Extensive Areas
- The provided values represent averages over large sections of land. Be prepared for variability in terrain that may not be captured by these averages.

### 📅 Data Currency
- The elevation data is sourced from the SRTM (Shuttle Radar Topography Mission), which is not frequently updated. Recent changes in the landscape may not be reflected.

### 🧭 Focused Analysis
- The analysis primarily covers slope and ruggedness. Other important factors, such as surface type, weather conditions, or obstacles not evident from elevation data, are not included.

## Findings

### Terrain Overview

The WABDR was divided into six sections, and the analysis revealed the following:

- **Steepness**: The slopes range from 9° to 15° on average.
- **Challenging Section**: The segment from Cashmere to Chelan stands out with an average slope of approximately 15° and the highest ruggedness score.
- **Gentler Terrain**: The northern section from Conconully to Canada is more forgiving, with an average slope around 9°.

### Key Observations

- The route generally becomes less challenging as you move northward.
- There are sections with very steep slopes, balanced by flatter areas that provide a reprieve.

### Implications

Whether you're a seasoned backcountry expert or new to the scene, the WABDR offers a diverse terrain that will keep you engaged throughout the journey.

## WABDR Terrain Summary

| Section | Avg. Slope | Ruggedness | Difficulty |
|---------|:----------:|:----------:|:----------:|
| Oregon Border to Packwood | 13.96° | 6.3990 | 🏔️🏔️🏔️ |
| Packwood to Ellensburg | 13.75° | 6.8401 | 🏔️🏔️🏔️ |
| Ellensburg to Cashmere | 11.01° | 4.9460 | 🏔️🏔️ |
| Cashmere to Chelan | 14.73° | 7.3343 | 🏔️🏔️🏔️🏔️ |
| Chelan to Conconully | 10.68° | 5.0800 | 🏔️🏔️ |
| Conconully to Canada | 9.62° | 4.7239 | 🏔️ |
