# MapCompare v 0.1
# Written by Waves
# This software is intended to be used to compare map times on CSGO's "Church of Citatsia" surf servers

from datetime import datetime
import fileinput


def get_times():

    times_list = []
    for line in fileinput.input():
        if line == "\n":
            fileinput.close()
            break
        times_list = times_list + line.replace("\n", " ").split(" ")
    # does some housekeeping to get rid of null strings
    for element in times_list:
        if element == "":
            times_list.remove(element)
    return times_list


def main():

    # This maps list is generated by makeMapList.py, and is complete as of 11/13/2016
    # If the server's list of maps is updated, the new maps must be added for this program to work properly
    # The best way to do this would be by using makeMapList.py with a player's times who has completed all maps
    noob_maps_list = ['surf_ace_fix,', 'surf_aircontrol_ksf,', 'surf_akai_final,', 'surf_and_destroy,',
                      'surf_beginner,', 'surf_calycate_csgo,', 'surf_classics,', 'surf_colours,', 'surf_colum_up,',
                      'surf_derpis_ksf,', 'surf_ethereal,', 'surf_forbidden_ways_ksf,', 'surf_funhouse_njv,',
                      'surf_grassland,', 'surf_kitsune,', 'surf_leet_xlbeta7z,', 'surf_legends_lite_gfl,',
                      'surf_lessons,', 'surf_life_of_duck_go,', 'surf_lullaby_ksf,', 'surf_lux,', 'surf_mesa,',
                      'surf_minuet_v1p,', 'surf_mom,', 'surf_newb_hazard_r1,', 'surf_pox,', 'surf_prelude_ksf,',
                      'surf_prime_time_r3vamp,', 'surf_rebel_resistance_njv,', 'surf_Rebel_scaz_njv,', 'surf_reprise,',
                      'surf_rookie,', 'surf_simpsons_go_rc2,', 'surf_spacejam,', 'surf_the_gloaming,',
                      'surf_trance_ksf,', 'surf_utopia_njv,', 'surf_water-run_banjo_skill,', 'surf_waterworks,',
                      'surf_year3000,']

    casual_maps_list = ['surf_ace_fix,', 'surf_amplitude_encore_nsf_v4,', 'surf_amplitude_light,', 'surf_atlas_1,',
                        'surf_b_r_o_x_x', 'surf_classics,', 'surf_classics2,', 'surf_colors_beta1,', 'surf_colours,',
                        'surf_coralis_ksf-,', 'surf_delusional_,', 'surf_eclipse,', 'surf_elites_v2,',
                        'surf_faint_fix,', 'surf_fruits,', 'surf_furios-,', 'surf_glass7,', 'surf_glass9,', 'surf_globalchaos,',
                        'surf_graphia,', 'surf_grassland,', 'surf_halloween_tf,', 'surf_happyhands_test,',
                        'surf_how2surf,', 'surf_hurrr,', 'surf_ing_njv,', 'surf_inspire,', 'surf_island,',
                        'surf_krow10,', 'surf_kz_protraining,', 'surf_lessons,', 'surf_lore_e,', 'surf_mesa_aether,',
                        'surf_mesa_mine,', 'surf_neo_njv,', 'surf_network_2008_final,', 'surf_newb_hazard_r1,',
                        'surf_not_so_sinister,', 'surf_ny_platinum,', 'surf_ny_superhappiest_b3,', 'surf_presmon_fix,',
                        'surf_psycho_njv,', 'surf_rainbow,', 'surf_rookie,', 'surf_simpsons_go_rc2,', 'surf_spacejam,',
                        'surf_sundown_njv,', 'surf_sunnyhappylove,', 'surf_sup_,', 'surf_syria_,', 'surf_tensile_njv,',
                        'surf_tomb_redone,', 'surf_vegetables,', 'surf_waterworks,', 'surf_wood,']

    skill_maps_list = ['surf_2012_beta12,', 'surf_acp,', 'surf_adtr_njv,', 'surf_aether,', 'surf_amateur_v2b_,',
                       'surf_amplitude_apex_njv,', 'surf_animals,', 'surf_anthropomorphic-,', 'surf_asrown-,',
                       'surf_ataque_final,', 'surf_auroia_njv,', 'surf_auroria_2,', 'surf_bbb,', 'surf_bob,',
                       'surf_boring,', 'surf_bork_nbv,', 'surf_calamity2,', 'surf_canisius,', 'surf_canisius2,',
                       'surf_catalyst2,', 'surf_christmas,', 'surf_color_njv,', 'surf_commune_too_beta5,',
                       'surf_compulsive_njv,', 'surf_concept_njv,', 'surf_creation,', 'surf_crystal,', 'surf_cyka,',
                       'surf_depressing,', 'surf_depths,', 'surf_diminsion_,', 'surf_doodles_njv,', 'surf_dusk,',
                       'surf_dynasty,', 'surf_elements_beta3,', 'surf_ember_sns,', 'surf_epic,', 'surf_eternal_beta,',
                       'surf_exocube,', 'surf_fast,', 'surf_flyin_fortress,', 'surf_healthy_e,', 'surf_heaven,',
                       'surf_hydrogen_v2_njv,', 'surf_imagine_fix,', 'surf_imex_njv,', 'surf_impact_njv,',
                       'surf_injection_njv,', 'surf_insideout,', 'surf_jenocide,', 'surf_kawaii,', 'surf_liberation,',
                       'surf_liberation2,', 'surf_lies,', 'surf_lighthouse,', 'surf_lithium-,', 'surf_lolrevlis2,',
                       'surf_mellow,', 'surf_methadone,', 'surf_missing_no,', 'surf_molstration,', 'surf_network_2013,',
                       'surf_ny_advance_nsf_v2,', 'surf_n_bhop_beta1,', 'surf_olympics_sns,', 'surf_omnibus_sns,',
                       'surf_orbion_x,', 'surf_overgrowth,', 'surf_palette_v2,', 'surf_pinkbash,',
                       'surf_plaguelands_beta7a,', 'surf_porn_fix,', 'surf_prosaic_njv,', 'surf_psi,',
                       'surf_quantum_njv,', 'surf_quattro-,', 'surf_quilavar-,', 'surf_razer_final,',
                       'surf_redemption_b1,', 'surf_refraxis,', 'surf_sanding,', 'surf_seaworld,', 'surf_sky_ages,',
                       'surf_smile,', 'surf_spectrum_njv,', 'surf_s_t_a_t_i_o_n,', 'surf_take1,', 'surf_thembrium_sns,',
                       'surf_this_njv,', 'surf_torque_,', 'surf_tron_njv,', 'surf_two_colour,', 'surf_ultimatum,',
                       'surf_velocity_nsf,', 'surf_voteforthisone,', 'surf_wazor,']

    print("Hello and welcome to MapCompare!")
    print("Now you can find out if you are better than your friends!")
    server = input("What server are you playing on?")
    if server.lower() == "skill":
        maps_list = skill_maps_list
    elif server.lower() == "casual":
        maps_list = casual_maps_list
    else:
        maps_list = noob_maps_list

    my_name = input("What is your name? ")
    other_name = input("Who are you comparing to today? ")

    print("Please enter your times. Enter a blank line to finish.")
    my_list = get_times()

    print("Please enter your opponent's times. Enter a blank line to finish.")
    other_list = get_times()

    # lazy code for debugging
    # print(my_list)
    # print(other_list)

    i = 0               # index relative to master map list
    my_i = 0            # index relative to user map list
    other_i = 0         # index relative to opponent map list
    my_wins = 0
    other_wins = 0
    my_beat = 0
    other_beat = 0
    both_fail = 0

    sum_maps = len(maps_list)
    my_max = len(my_list)
    other_max = len(other_list)

    while i < sum_maps:
        # more lazy debugging code ;3
        # print("i equals: " + str(i))
        # print("my_i equals: " + str(my_i))
        # print("other_i equals: " + str(other_i))
        # print("Player one is on: " + my_list[my_i])
        # print("Player two is on : " + other_list[other_i])

        if (my_i < my_max) and (other_i < other_max) and (maps_list[i] == my_list[my_i]) and (maps_list[i] == other_list[other_i]):  # if both users have the current map
            my_time = datetime.strptime(my_list[my_i+2].replace(",", "0000"), "%M:%S:%f") # gets rid of a trailing comma, sets up microseconds right
            other_time = datetime.strptime(other_list[other_i+2].replace(",", "0000"), "%M:%S:%f")
            if my_time < other_time:  # remember: a smaller time is a faster one.
                print("They both have beaten " + maps_list[i] + " but " + my_name + " is " +
                      str(other_time - my_time) + " faster than " + other_name)
                my_wins += 1

            elif my_time >= other_time:
                print("They both have beaten " + maps_list[i] + " but " + other_name + " is " +
                      str(my_time - other_time) + " faster than " + my_name)
                other_wins += 1
            my_i += 5
            other_i += 5

        elif (my_i < my_max) and (maps_list[i] == my_list[my_i]):
            print("Only " + my_name + " has beaten " + maps_list[i])
            my_i += 5
            my_beat += 1

        elif (other_i < other_max) and (maps_list[i] == other_list[other_i]):
            print("Only " + other_name + " has beaten " + maps_list[i])
            other_i += 5
            other_beat += 1

        else:
            print("Neither player has beaten " + maps_list[i] + " ... git gud")
            both_fail += 1

        i += 1

    print("=====SUMMARY=====")
    print(str(i))
    print(my_name + " has beaten " + other_name + "'s times on " + str(my_wins) + " maps")
    print(my_name + " has beaten " + str(my_beat) + " maps which " + other_name + " has not beat")
    print(other_name + " has beaten " + my_name + "'s times on " + str(other_wins) + " maps")
    print(other_name + " has beaten " + str(other_beat) + " maps which " + my_name + " has not beat")
    print("There are " + str(both_fail) + " maps which neither player has beat")

main()
