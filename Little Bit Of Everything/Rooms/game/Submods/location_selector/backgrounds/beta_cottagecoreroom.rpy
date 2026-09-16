init -1 python: 
    mas_background_def = MASFilterableBackground(
        "submod_beta_cottageroom",
        "Cottagecore Room",
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_beta_cottageroom_day",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_beta_cottageroom_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_beta_cottageroom_sunset",
            }),
        ),
        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),
        hide_calendar=True,
        unlocked=True,
        entry_pp=store.mas_background._def_background_entry,
        exit_pp=store.mas_background._def_background_exit,
    )

    #Now load data
    store.mas_background.loadMBGData()


init 1 python in mas_background:

    # verify all backgrounds
    for flt_bg in BACKGROUND_MAP.itervalues():
        flt_bg.verify()

image submod_beta_cottageroom_day = "mod_assets/location/beta_cottageroom/beta_cottageroom-day.png"
image submod_beta_cottageroom_night = "mod_assets/location/beta_cottageroom/beta_cottageroom-night.png"
image submod_beta_cottageroom_sunset = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/beta_cottageroom/beta_cottageroom-sunset.png"
)