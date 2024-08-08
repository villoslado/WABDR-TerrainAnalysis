# WABDR-TerrainAnalysis 🏔️🚙

Hi fellow off-road enthusiasts! 👋

Ever wondered what the Washington Backcountry Discovery Route (WABDR) really looks like on paper? Well, that's how this little project was born.

## What's this all about?

I'm a big fan of backcountry adventures and off-roading, and I thought it'd be cool to dive into some data about the WABDR. This project is all about playing with geographical data to get some insights about the route.

## What are we looking at?

We're breaking down the WABDR into six sections and analyzing three key factors for each:

1. 📐 **Slope**: How steep is this bad boy? This tells us about the incline we're dealing with.

2. 🧭 **Aspect**: Which way does the slope face? This can give us hints about stuff like sun exposure or potential snow melt.

3. 🏔️ **Terrain Ruggedness Index (TRI)**: Fancy term for "how bumpy is it?" Higher TRI = more challenging terrain.

## The stuff we're using

We're tapping into some cool tech here:

- Google Earth Engine for grabbing elevation data 🛰️
- Python to crunch numbers 🐍
- Some geospatial libraries to make sense of it all 🗺️

## Why?

This project is all about combining my love for off-roading with some data fun. The insights we get could be useful for planning trips, understanding the challenges of different sections, or just geeking out over terrain. 🤓

## How?

To use these scripts:

Run `bdr_data_downloader.py` first. This might take a while. Once all data is downloaded, run `bdr_terrain_analyzer.py` to process the data and get results.

## 🚨 Things to Keep in Mind

While we've done our best, there are a few things you should know:

### 📏 Resolution Limitations
- Our data has a resolution of about 30m per pixel. We missed some finer details of the terrain.

### 🗺️ Averaging Over Large Areas
- We're giving you average values for some pretty big stretches of land.
- Don't be surprised if you hit patches that are way steeper or flatter than the average we've shown.

### 📅 Data Freshness
- We're using elevation data from the SRTM (Shuttle Radar Topography Mission). This data isn't updated frequently, so any recent changes to the landscape won't be reflected.

### 🧭 Limited Factors
- Our analysis focuses mainly on slope and ruggedness. There are lots of other factors that make a route challenging or easy - like surface type, weather conditions, or obstacles that don't show up in elevation data.

## What We Found Out

Here's a summary:

### The Lay of the Land

We sliced the WABDR into six sections and took a look at each one. Here's what we discovered:

- **Steepness**: On average, we're looking at slopes between 9° and 15°.
- **Tough Stuff**: The stretch from Cashmere to Chelan is the beast, with an average slope of about 15° and highest ruggedness score.
- **Easier Riding**: If you're easing into it, the northern bit from Conconully to Canada is your friend. It's the gentlest, with slopes averaging around 9°.

### Factoids

- The route generally gets a bit easier as you head north.
- We found some spots with veeery steep slopes. There's plenty of flat ground too, perfect for catching your breath.

### What It All Means

Whether you're a veteran or a newbie like me to the backcountry scene, the WABDR's got something for everyone. It's a rollercoaster of terrain that'll keep you on your wheels the whole way through.

The WABDR in a nutshell.

## WABDR Terrain Summary

| Section | Avg. Slope | Ruggedness | Difficulty |
|---------|:----------:|:----------:|:----------:|
| Oregon Border to Packwood | 13.96° | 6.3990 | 🏔️🏔️🏔️ |
| Packwood to Ellensburg | 13.75° | 6.8401 | 🏔️🏔️🏔️ |
| Ellensburg to Cashmere | 11.01° | 4.9460 | 🏔️🏔️ |
| Cashmere to Chelan | 14.73° | 7.3343 | 🏔️🏔️🏔️🏔️ |
| Chelan to Conconully | 10.68° | 5.0800 | 🏔️🏔️ |
| Conconully to Canada | 9.62° | 4.7239 | 🏔️ |
