# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# marine_terrestrial_model.py
# Created on: 2015-01-28 13:26:31.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: marine_terrestrial_model <Enter_DEM_of_AOI> <Dude__Select_the_point_of_origin> <Select_the_factor_used_to_augment_lowland_features> <mykinai__2_> <weight_for_main_cost__decimal_> <Maximum_effect_distance> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

# Script arguments
Enter_DEM_of_AOI = arcpy.GetParameterAsText(0)
if Enter_DEM_of_AOI == '#' or not Enter_DEM_of_AOI:
    Enter_DEM_of_AOI = "aoidem" # provide a default value if unspecified

Dude__Select_the_point_of_origin = arcpy.GetParameterAsText(1)
if Dude__Select_the_point_of_origin == '#' or not Dude__Select_the_point_of_origin:
    Dude__Select_the_point_of_origin = "O:\\Default.gdb\\kolonna" # provide a default value if unspecified

Select_the_factor_used_to_augment_lowland_features = arcpy.GetParameterAsText(2)
if Select_the_factor_used_to_augment_lowland_features == '#' or not Select_the_factor_used_to_augment_lowland_features:
    Select_the_factor_used_to_augment_lowland_features = "10" # provide a default value if unspecified

mykinai__2_ = arcpy.GetParameterAsText(3)
if mykinai__2_ == '#' or not mykinai__2_:
    mykinai__2_ = "O:\\Default.gdb\\mykinai" # provide a default value if unspecified

weight_for_main_cost__decimal_ = arcpy.GetParameterAsText(4)
if weight_for_main_cost__decimal_ == '#' or not weight_for_main_cost__decimal_:
    weight_for_main_cost__decimal_ = "0.7" # provide a default value if unspecified

Maximum_effect_distance = arcpy.GetParameterAsText(5)
if Maximum_effect_distance == '#' or not Maximum_effect_distance:
    Maximum_effect_distance = "2" # provide a default value if unspecified

# Local variables:
constant_value___1 = "1"
aoidem_copy = Enter_DEM_of_AOI
flow_acc = aoidem_copy
flow_accum_1 = flow_acc
flow_div_slop = flow_accum_1
moist_index = flow_div_slop
Greater_mois1 = moist_index
boggy_bits = Greater_mois1
Times_boggy = boggy_bits
dem_n_bog = Times_boggy
dem_n_bog_slp = dem_n_bog
dem_x_pi = dem_n_bog_slp
demxpi_by_180 = dem_x_pi
Tan_demxpi_b1 = demxpi_by_180
effort = Tan_demxpi_b1
terra_cost_rev = effort
CostDisterra_myki = terra_cost_rev
terrapthkorphmyk = CostDisterra_myki
effort_path_korph2myc__3_ = terrapthkorphmyk
terrabklnkmyk = terra_cost_rev
terra_cost_masked = terra_cost_rev
terra_marine_cost = terra_cost_masked
cd_apr2 = terra_marine_cost
path_dec_naismith = cd_apr2
name_the_first_path = path_dec_naismith
cost_backlnkapr2 = terra_marine_cost
costsurf_main_culturally_adjustedtimes = terra_cost_rev
costsurf_main_cultadjusted_land = costsurf_main_culturally_adjustedtimes
costsurf_mainadjusted = costsurf_main_cultadjusted_land
costdist_main = costsurf_mainadjusted
costpath_cultweighted = costdist_main
costpath_cultweighted_line = costpath_cultweighted
backlink_main = costsurf_mainadjusted
costsurf_main_detractculturally_adjustedtimes = terra_cost_rev
costsurf_main_detractcultadjusted_land = costsurf_main_detractculturally_adjustedtimes
costsurf_maindetractadjusted = costsurf_main_detractcultadjusted_land
costdistdetract_main = costsurf_maindetractadjusted
costpath_detractcultweighted = costdistdetract_main
costpath_detractcultweighted_line = costpath_detractcultweighted
backlinkdetract_main = costsurf_maindetractadjusted
costsurf_main_attractdetract_adjustedtimes = terra_cost_rev
costsurf_main_attractdetract_land = costsurf_main_attractdetract_adjustedtimes
costsurf_main_attractdetractadjusted = costsurf_main_attractdetract_land
costdist_main_attractdetract = costsurf_main_attractdetractadjusted
costpath_attractdetract = costdist_main_attractdetract
costpath_attractdetract_line = costpath_attractdetract
backlink_main_attractdetract = costsurf_main_attractdetractadjusted
rise_of_all_aoi = Tan_demxpi_b1
nais_penalties_5to12 = rise_of_all_aoi
naismith_rule = nais_penalties_5to12
naismith_masked = naismith_rule
naismith_wind_cost = naismith_masked
costdist_korphos__2_ = naismith_wind_cost
costdist_korphos_zero = costdist_korphos__2_
dist_percent_korphos__2_ = costdist_korphos_zero
costdist_korphos_weighted = dist_percent_korphos__2_
costdist_korphos_onesies = costdist_korphos_weighted
costdist_attractors_mosaicd_noisthmia = costdist_korphos_onesies
costdist_attractors_zeroed = costdist_attractors_mosaicd_noisthmia
costdist_attractdetractors_mosaicd = costdist_attractors_zeroed
costdist_attractdetract_onesies = costdist_attractdetractors_mosaicd
dist_detractpercent_korphos = costdist_korphos_zero
costdist_detractkorphos = dist_detractpercent_korphos
Output_backlink_raster__9_ = naismith_wind_cost
costdist_epidavros = naismith_wind_cost
costdist_epidavros_zero = costdist_epidavros
dist_percent_epidavros__2_ = costdist_epidavros_zero
costdist_epidavros_weighted = dist_percent_epidavros__2_
costdist_epidavros_onesies = costdist_epidavros_weighted
dist_detractpercent_epidavros = costdist_epidavros_zero
costdist_detractepidavros = dist_detractpercent_epidavros
Output_backlink_raster__10_ = naismith_wind_cost
costdist_isthmia = naismith_wind_cost
costdist_isthmia_zero = costdist_isthmia
dist_percent_isthmia = costdist_isthmia_zero
costdist_isthmia_weighted = dist_percent_isthmia
costdist_isthmia_onesies = costdist_isthmia_weighted
dist_detractpercent_isthmia = costdist_isthmia_zero
costdist_detractisthmia = dist_detractpercent_isthmia
costdist_detractors_mosaicd_isthmia = costdist_detractisthmia
costdist_detractors_zeroed = costdist_detractors_mosaicd_isthmia
Output_backlink_raster__11_ = naismith_wind_cost
land1water0 = naismith_masked
land0water1 = naismith_masked
costsurf_main_water = land0water1
nais_penalties_more12 = rise_of_all_aoi
LessThan12 = dem_n_bog_slp
mor5less12slp = LessThan12
v5to12_penalty = mor5less12slp
Greaterthan_12 = dem_n_bog_slp
ms_more12 = Greaterthan_12
Output_raster__3_ = dem_n_bog_slp
slope__3_ = aoidem_copy
slope_plus1 = slope__3_
windata_mask_n_ = aoidem_copy
wind_knots2ms_n_ = windata_mask_n_
ovrwindeffrt = wind_knots2ms_n_
land_mask = aoidem_copy
PI = "3.141592654"
v180 = "180"
v0_017455 = "0.017455065"
conversion_number__knots_2_m_sec = "0.514444444444444"
v5 = "5"
v12 = "12"
v1_998 = "1.998"
v6__2_ = "6"
v21_58828612 = "21.58828612"
korphos = "O:\\Default.gdb\\korphos"
Input_raster_or_constant_value_2__2_ = "0"
krig_apr_0600 = "O:\\Default.gdb\\krig_apr_0600"
epidavros = "O:\\default.gdb\\epidavros"
isthmia = "O:\\default.gdb\\isthmia"
default_gdb__2_ = "O:\\default.gdb"
default_gdb__3_ = "O:\\default.gdb"
wind_rast_n_ = "D:\\Users\\newhardj\\Documents\\ArcGIS\\Default.gdb\\krig_apr_0600_CopyRaster"

# Process: Copy Raster
# arcpy.CopyRaster_management(Enter_DEM_of_AOI, aoidem_copy, "", "", "", "NONE", "NONE", "", "NONE", "NONE")

# Process: Greater Than (2)
# arcpy.gp.GreaterThan_sa(aoidem_copy, Input_raster_or_constant_value_2__2_, land_mask)

# Process: Flow Accumulation
# arcpy.gp.FlowAccumulation_sa(aoidem_copy, flow_acc, "", "FLOAT")

# Process: Plus
# arcpy.gp.Plus_sa(flow_acc, constant_value___1, flow_accum_1)

# Process: Slope
# arcpy.gp.Slope_sa(aoidem_copy, slope__3_, "DEGREE", "1")

# Process: Plus (2)
# arcpy.gp.Plus_sa(slope__3_, constant_value___1, slope_plus1)

# Process: Divide
# arcpy.gp.Divide_sa(flow_accum_1, slope_plus1, flow_div_slop)

# Process: Ln
# arcpy.gp.Ln_sa(flow_div_slop, moist_index)

# Process: Greater Than
# arcpy.gp.GreaterThan_sa(moist_index, Input_raster_or_constant_value_2__2_, Greater_mois1)

# Process: Times
# arcpy.gp.Times_sa(Greater_mois1, moist_index, boggy_bits)

# Process: Times (2)
# arcpy.gp.Times_sa(boggy_bits, Select_the_factor_used_to_augment_lowland_features, Times_boggy)

# Process: Plus (3)
# arcpy.gp.Plus_sa(Times_boggy, aoidem_copy, dem_n_bog)

# Process: Slope (4)
# arcpy.gp.Slope_sa(dem_n_bog, dem_n_bog_slp, "DEGREE", "1")

# Process: Times (3)
arcpy.gp.Times_sa(dem_n_bog_slp, PI, dem_x_pi)

# Process: Divide (2)
arcpy.gp.Divide_sa(dem_x_pi, v180, demxpi_by_180)

# Process: Tan
arcpy.gp.Tan_sa(demxpi_by_180, Tan_demxpi_b1)

# Process: Divide (3)
arcpy.gp.Divide_sa(Tan_demxpi_b1, v0_017455, effort)

# Process: Greater Than Equal (2)
arcpy.gp.GreaterThanEqual_sa(dem_n_bog_slp, v5, Output_raster__3_)

# Process: Less Than (2)
arcpy.gp.LessThan_sa(dem_n_bog_slp, v12, LessThan12)

# Process: Times (10)
arcpy.gp.Times_sa(Output_raster__3_, LessThan12, mor5less12slp)

# Process: Times (11)
arcpy.gp.Times_sa(mor5less12slp, v1_998, v5to12_penalty)

# Process: Times (16)
arcpy.gp.Times_sa(Tan_demxpi_b1, v21_58828612, rise_of_all_aoi)

# Process: Times (9)
arcpy.gp.Times_sa(v5to12_penalty, rise_of_all_aoi, nais_penalties_5to12)

# Process: Greater Than Equal
arcpy.gp.GreaterThanEqual_sa(dem_n_bog_slp, v12, Greaterthan_12)

# Process: Times (13)
arcpy.gp.Times_sa(v6__2_, Greaterthan_12, ms_more12)

# Process: Times (12)
arcpy.gp.Times_sa(rise_of_all_aoi, ms_more12, nais_penalties_more12)

# Process: sums all penalties for naismith's rule
arcpy.gp.RasterCalculator_sa("\"%nais_penalties_5to12%\" + \"%nais_penalties_more12%\" + 15.12", naismith_rule)

# Process: Weighted Sum
arcpy.gp.WeightedSum_sa("O:\\Default.gdb\\effort VALUE 0.5;O:\\Default.gdb\\naismith_rule VALUE 0.5", terra_cost_rev)

# Process: Times (7)
arcpy.gp.Times_sa(land_mask, terra_cost_rev, terra_cost_masked)

# Process: Copy Raster (2)
arcpy.CopyRaster_management(krig_apr_0600, wind_rast_n_, "", "", "", "NONE", "NONE", "", "NONE", "NONE")

# Process: Extract by Mask
arcpy.gp.ExtractByMask_sa(wind_rast_n_, aoidem_copy, windata_mask_n_)

# Process: convert knots to m/s
arcpy.gp.Times_sa(windata_mask_n_, conversion_number__knots_2_m_sec, wind_knots2ms_n_)

# Process: Divide (7)
arcpy.gp.Divide_sa(v21_58828612, wind_knots2ms_n_, ovrwindeffrt)

# Process: Raster Calculator
arcpy.gp.RasterCalculator_sa("Con(\"%terra_cost_masked%\">0,\"%terra_cost_masked%\",\"%ovrwindeffrt%\")", terra_marine_cost)

# Process: Cost Distance (2)
arcpy.gp.CostDistance_sa(mykinai__2_, terra_marine_cost, cd_apr2, "", cost_backlnkapr2)

# Process: Cost Path (3)
arcpy.gp.CostPath_sa(Dude__Select_the_point_of_origin, cd_apr2, cost_backlnkapr2, path_dec_naismith, "EACH_CELL", "Id")

# Process: Raster to Polyline (2)
arcpy.RasterToPolyline_conversion(path_dec_naismith, name_the_first_path, "ZERO", "0", "SIMPLIFY", "Value")

# Process: Cost Distance (9)
arcpy.gp.CostDistance_sa(mykinai__2_, terra_cost_rev, CostDisterra_myki, "", terrabklnkmyk)

# Process: Cost Path (6)
arcpy.gp.CostPath_sa(korphos, CostDisterra_myki, terrabklnkmyk, terrapthkorphmyk, "EACH_CELL", "Id")

# Process: Raster to Polyline (6)
arcpy.RasterToPolyline_conversion(terrapthkorphmyk, effort_path_korph2myc__3_, "ZERO", "0", "SIMPLIFY", "VALUE")

# Process: Times (18)
arcpy.gp.Times_sa(naismith_rule, land_mask, naismith_masked)

# Process: Raster Calculator (4)
arcpy.gp.RasterCalculator_sa("Con(\"%naismith_masked%\" > 0,\"%naismith_masked%\",\"%ovrwindeffrt%\")", naismith_wind_cost)

# Process: Cost Distance (13)
arcpy.gp.CostDistance_sa(korphos, naismith_wind_cost, costdist_korphos__2_, "", Output_backlink_raster__9_)

# Process: Raster Calculator (10)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_korphos (2)%\" < (float(%Maximum effect distance%)*60*60*21.58),\"%costdist_korphos (2)%\",0)", costdist_korphos_zero)

# Process: Raster Calculator (9)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_korphos_zero%\">0,(\"%costdist_korphos_zero%\"/(%Maximum effect distance%*60*60*21.58)),0)", dist_percent_korphos__2_)

# Process: Times (20)
arcpy.gp.Times_sa(weight_for_main_cost__decimal_, dist_percent_korphos__2_, costdist_korphos_weighted)

# Process: Raster Calculator (11)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_korphos_weighted%\"<.0001,1, \"%costdist_korphos_weighted%\")", costdist_korphos_onesies)

# Process: Cost Distance (15)
arcpy.gp.CostDistance_sa(epidavros, naismith_wind_cost, costdist_epidavros, "", Output_backlink_raster__10_)

# Process: Raster Calculator (14)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_epidavros%\" < (float(%Maximum effect distance%)*60*60*21.58),\"%costdist_epidavros%\",0)", costdist_epidavros_zero)

# Process: Raster Calculator (15)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_epidavros_zero%\">0,(\"%costdist_epidavros_zero%\"/(%Maximum effect distance%*60*60*21.58)),0)", dist_percent_epidavros__2_)

# Process: Times (24)
arcpy.gp.Times_sa(weight_for_main_cost__decimal_, dist_percent_epidavros__2_, costdist_epidavros_weighted)

# Process: Raster Calculator (19)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_epidavros_weighted%\"<.0001,1, \"%costdist_epidavros_weighted%\")", costdist_epidavros_onesies)

# Process: Mosaic To New Raster (2)
arcpy.MosaicToNewRaster_management("O:\\Default.gdb\\costdist_korphos_onesies;O:\\default.gdb\\costdist_epidavros_onesies", default_gdb__2_, "costdist_attractors_mosaicd_noisthmia", "PROJCS['WGS_1984_Cylindrical_Equal_Area',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Cylindrical_Equal_Area'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],UNIT['Meter',1.0]]", "32_BIT_FLOAT", "", "1", "MINIMUM", "FIRST")

# Process: Times (21)
arcpy.gp.Times_sa(costdist_attractors_mosaicd_noisthmia, terra_cost_rev, costsurf_main_culturally_adjustedtimes)

# Process: Raster Calculator (12)
arcpy.gp.RasterCalculator_sa("Con(\"%naismith_masked%\">0,1,0)", land1water0)

# Process: Times (22)
arcpy.gp.Times_sa(costsurf_main_culturally_adjustedtimes, land1water0, costsurf_main_cultadjusted_land)

# Process: Raster Calculator (13)
arcpy.gp.RasterCalculator_sa("Con(\"%naismith_masked%\">0,0,1)", land0water1)

# Process: Times (23)
arcpy.gp.Times_sa(land0water1, ovrwindeffrt, costsurf_main_water)

# Process: Plus (5)
arcpy.gp.Plus_sa(costsurf_main_cultadjusted_land, costsurf_main_water, costsurf_mainadjusted)

# Process: Cost Distance (14)
arcpy.gp.CostDistance_sa(mykinai__2_, costsurf_mainadjusted, costdist_main, "", backlink_main)

# Process: Cost Path (2)
arcpy.gp.CostPath_sa(Dude__Select_the_point_of_origin, costdist_main, backlink_main, costpath_cultweighted, "EACH_CELL", "Id")

# Process: Raster to Polyline (7)
arcpy.RasterToPolyline_conversion(costpath_cultweighted, costpath_cultweighted_line, "ZERO", "0", "SIMPLIFY", "Value")

# Process: Cost Distance (16)
arcpy.gp.CostDistance_sa(isthmia, naismith_wind_cost, costdist_isthmia, "", Output_backlink_raster__11_)

# Process: Raster Calculator (16)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_isthmia%\" < (float(%Maximum effect distance%)*60*60*21.58),\"%costdist_isthmia%\",0)", costdist_isthmia_zero)

# Process: Raster Calculator (17)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_isthmia_zero%\">0,(\"%costdist_isthmia_zero%\"/(%Maximum effect distance%*60*60*21.58)),0)", dist_percent_isthmia)

# Process: Times (25)
arcpy.gp.Times_sa(weight_for_main_cost__decimal_, dist_percent_isthmia, costdist_isthmia_weighted)

# Process: Raster Calculator (20)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_isthmia_weighted%\"<.0001,1, \"%costdist_isthmia_weighted%\")", costdist_isthmia_onesies)

# Process: Raster Calculator (22)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_epidavros_zero%\">0,(1-(\"%costdist_epidavros_zero%\"/(%Maximum effect distance%*60*60*21.58))),0)", dist_detractpercent_epidavros)

# Process: Raster Calculator (25)
arcpy.gp.RasterCalculator_sa("1+(float(%weight for main cost (decimal)%)*\"%dist_detractpercent_epidavros%\")", costdist_detractepidavros)

# Process: Raster Calculator (21)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_korphos_zero%\">0,(1-(\"%costdist_korphos_zero%\"/(%Maximum effect distance%*60*60*21.58))),0)", dist_detractpercent_korphos)

# Process: Raster Calculator (26)
arcpy.gp.RasterCalculator_sa("1+(float(%weight for main cost (decimal)%)*\"%dist_detractpercent_korphos%\")", costdist_detractkorphos)

# Process: Raster Calculator (23)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_isthmia_zero%\">0,(1-(\"%costdist_isthmia_zero%\"/(%Maximum effect distance%*60*60*21.58))),0)", dist_detractpercent_isthmia)

# Process: Raster Calculator (24)
arcpy.gp.RasterCalculator_sa("1+(float(%weight for main cost (decimal)%)*\"%dist_detractpercent_isthmia%\")", costdist_detractisthmia)

# Process: Mosaic To New Raster (3)
arcpy.MosaicToNewRaster_management("O:\\default.gdb\\costdist_detractisthmia", default_gdb__2_, "costdist_detractors_mosaicd_isthmia", "PROJCS['WGS_1984_Cylindrical_Equal_Area',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Cylindrical_Equal_Area'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],UNIT['Meter',1.0]]", "32_BIT_FLOAT", "", "1", "MAXIMUM", "FIRST")

# Process: Times (26)
arcpy.gp.Times_sa(costdist_detractors_mosaicd_isthmia, terra_cost_rev, costsurf_main_detractculturally_adjustedtimes)

# Process: Times (27)
arcpy.gp.Times_sa(land1water0, costsurf_main_detractculturally_adjustedtimes, costsurf_main_detractcultadjusted_land)

# Process: Plus (7)
arcpy.gp.Plus_sa(costsurf_main_water, costsurf_main_detractcultadjusted_land, costsurf_maindetractadjusted)

# Process: Cost Distance (17)
arcpy.gp.CostDistance_sa(mykinai__2_, costsurf_maindetractadjusted, costdistdetract_main, "", backlinkdetract_main)

# Process: Cost Path (7)
arcpy.gp.CostPath_sa(Dude__Select_the_point_of_origin, costdistdetract_main, backlinkdetract_main, costpath_detractcultweighted, "EACH_CELL", "Id")

# Process: Raster to Polyline (8)
arcpy.RasterToPolyline_conversion(costpath_detractcultweighted, costpath_detractcultweighted_line, "ZERO", "0", "SIMPLIFY", "Value")

# Process: Raster Calculator (28)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_detractors_mosaicd_isthmia%\" == 1,0, \"%costdist_detractors_mosaicd_isthmia%\")", costdist_detractors_zeroed)

# Process: Raster Calculator (29)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_attractors_mosaicd_noisthmia%\" == 1,0, \"%costdist_attractors_mosaicd_noisthmia%\")", costdist_attractors_zeroed)

# Process: Mosaic To New Raster (4)
arcpy.MosaicToNewRaster_management("O:\\default.gdb\\costdist_detractors_zeroed;O:\\default.gdb\\costdist_attractors_zeroed", default_gdb__3_, "costdist_attractdetractors_mosaicd", "PROJCS['WGS_1984_Cylindrical_Equal_Area',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Cylindrical_Equal_Area'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],UNIT['Meter',1.0]]", "32_BIT_FLOAT", "", "1", "MAXIMUM", "FIRST")

# Process: Raster Calculator (27)
arcpy.gp.RasterCalculator_sa("Con(\"%costdist_attractdetractors_mosaicd%\" == 0,1, \"%costdist_attractdetractors_mosaicd%\")", costdist_attractdetract_onesies)

# Process: Times (28)
arcpy.gp.Times_sa(costdist_attractdetract_onesies, terra_cost_rev, costsurf_main_attractdetract_adjustedtimes)

# Process: Times (29)
arcpy.gp.Times_sa(land1water0, costsurf_main_attractdetract_adjustedtimes, costsurf_main_attractdetract_land)

# Process: Plus (8)
arcpy.gp.Plus_sa(costsurf_main_water, costsurf_main_attractdetract_land, costsurf_main_attractdetractadjusted)

# Process: Cost Distance (18)
arcpy.gp.CostDistance_sa(mykinai__2_, costsurf_main_attractdetractadjusted, costdist_main_attractdetract, "", backlink_main_attractdetract)

# Process: Cost Path (8)
arcpy.gp.CostPath_sa(Dude__Select_the_point_of_origin, costdist_main_attractdetract, backlink_main_attractdetract, costpath_attractdetract, "EACH_CELL", "Id")

# Process: Raster to Polyline (9)
arcpy.RasterToPolyline_conversion(costpath_attractdetract, costpath_attractdetract_line, "ZERO", "0", "SIMPLIFY", "Value")

