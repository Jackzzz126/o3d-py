#!/usr/bin/env python
# -*- coding:utf-8 -*-

import open3d as o3d
import argparse
import sys
import time, datetime
import json

sys.path.append("./util")
from file import check_folder_structure
from initialize_config import initialize_config

import color_log as clog

if __name__ == "__main__":
    o3d.utility.set_verbosity_level(o3d.utility.VerbosityLevel.Always)
    parser = argparse.ArgumentParser(description="Reconstruction test")
    parser.add_argument(
        "--make",
        help="Step 1) make fragments from RGBD sequence",
        action="store_true")
    parser.add_argument(
        "--register",
        help="Step 2) register all fragments to detect loop closure",
        action="store_true")
    parser.add_argument(
        "--refine",
        help="Step 3) refine rough registrations",
        action="store_true")
    parser.add_argument(
        "--integrate",
        help="Step 4) integrate the whole RGBD sequence to make final mesh",
        action="store_true")
    parser.add_argument(
        "--debug_mode",
        help="turn on debug mode",
        action="store_true")
    args = parser.parse_args()
    if not args.make and \
            not args.register and \
            not args.refine and \
            not args.integrate:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # check folder structure
    with open("./config.json") as json_file:
        config = json.load(json_file)
        initialize_config(config)
        check_folder_structure(config["path_dataset"])
    assert config is not None

    clog.debug("Configuration")
    clog.debug("====================================")
    for key, val in config.items():
        clog.debug("%40s :%s" % (key, str(val)))

    times = [0, 0, 0, 0]
    if args.make:
        clog.debug("Make")
        clog.debug("====================================")
        start_time = time.time()
        import make_fragments
        make_fragments.run(config)
        times[0] = time.time() - start_time
    #if args.register:
    #    start_time = time.time()
    #    import register_fragments
    #    register_fragments.run(config)
    #    times[1] = time.time() - start_time
    #if args.refine:
    #    start_time = time.time()
    #    import refine_registration
    #    refine_registration.run(config)
    #    times[2] = time.time() - start_time
    #if args.integrate:
    #    start_time = time.time()
    #    import integrate_scene
    #    integrate_scene.run(config)
    #    times[3] = time.time() - start_time

    clog.debug("Elapsed time (in h:m:s)")
    clog.debug("====================================")
    clog.debug("- Making fragments    %s" % datetime.timedelta(seconds=times[0]))
    clog.debug("- Register fragments  %s" % datetime.timedelta(seconds=times[1]))
    clog.debug("- Refine registration %s" % datetime.timedelta(seconds=times[2]))
    clog.debug("- Integrate frames    %s" % datetime.timedelta(seconds=times[3]))
    clog.debug("- Total               %s" % datetime.timedelta(seconds=sum(times)))
    sys.stdout.flush()
