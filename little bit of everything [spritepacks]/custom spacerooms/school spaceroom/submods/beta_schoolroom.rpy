init -1 python: 
    mas_background_def = MASFilterableBackground(
        "submod_beta_schoolroom",
        "School Room",
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_beta_schoolroom_day",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_beta_schoolroom_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_beta_schoolroom_sunset",
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
        entry_pp=store.mas_background._beta_schoolroom_bg_entry,
        exit_pp=store.mas_background._beta_schoolroom_bg_exit,
    )

    #Now load data
    store.mas_background.loadMBGData()

init -2 python in mas_background:
    def _beta_schoolroom_bg_entry(_old, **kwargs):

        if kwargs.get("startup"):
            pass
        
        store.monika_chr.tablechair.table = "SS"
        store.monika_chr.tablechair.chair = "SS"

        #IF THIS IS NOT A FURNISHED SPACEROOM, COMMENT THESE TWO LINES
        if store.seen_event("mas_monika_islands"):
            store.mas_unlockEVL("mas_monika_islands", "EVE")

    def _beta_schoolroom_bg_exit(_new, **kwargs):
        store.mas_lockEVL("mas_monika_islands", "EVE")

        #COMMENT(#) IF NOT NEEDED
        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

init 1 python in mas_background:
    # verify all backgrounds
    for flt_bg in BACKGROUND_MAP.itervalues():
        flt_bg.verify()


image submod_beta_schoolroom_day = "mod_assets/location/beta_schoolroom/beta_schoolroom-day.png"
image submod_beta_schoolroom_night = "mod_assets/location/beta_schoolroom/beta_schoolroom-night.png"
image submod_beta_schoolroom_sunset = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/beta_schoolroom/beta_schoolroom-sunset.png"
)