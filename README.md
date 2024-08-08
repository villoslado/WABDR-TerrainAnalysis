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
