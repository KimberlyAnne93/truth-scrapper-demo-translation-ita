default persistent.text_animations = True

init python:

    # Custom text shake shader so that it applies to individual letters.
    # You can modify u__strength to make it less or more strong.
    renpy.register_textshader(
        "text_shake",
        vertex_functions = """
        float random(vec2 st)
        {
            return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);
        }
        float map(float value, float min1, float max1, float min2, float max2) {
            return min2 + (value - min1) * (max2 - min2) / (max1 - min1);
            }
        float lerp(float a, float b, float t)
        {
            return (1 - t) * a + t * b;
        }
        """,
        variables = """
        uniform float u__delay;
        uniform float u__offset;
        uniform float u_text_slow_time;
        uniform float u_text_to_drawable;
        uniform float u_time;
        uniform float u__strength;
        uniform vec2 u_text_offset;
        uniform vec4 u_random;
        uniform float u_text_depth;
        attribute vec2 a_text_center;
        attribute float a_text_min_time;
        attribute vec4 a_position;
        attribute float a_text_index;

        """,

        vertex_60 = """
        vec2 randIndex = vec2(random(vec2(a_text_center.x * (u_time), -a_text_center.y * (u_time))), random(vec2(a_text_center.x * (u_time), a_text_center.y * (u_time))));
        float randZoom = map(randIndex.x, 0.0, 1.0, 0.7, 1.1);
        //gl_Position.xy = mix(a_text_center + (gl_Position.xy - a_text_center) * randZoom, gl_Position.xy, randZoom);

        
        vec2 jitter = vec2(4, 3) * u_text_to_drawable * u__strength;
        gl_Position.xy += jitter * randIndex - jitter / 2.0;

        """,

        fragment_400 = """
        
        if (u_text_depth != 0.0)
        {
            gl_FragColor = vec4(gl_FragColor.rgb, gl_FragColor.a * 0.95);
        }
        """,
        redraw = 0.2,
        u__strength = 1.3
    )

    ## TAG DEFINITIONS
    ## Change the default values for the tags here! for example if you want to adjust the wave tag's movement, change line 67 to 
    ## u"shader=wave:u__amplitude=10.0:u__frequency=0.8"
    ## 10.0 is the amplitude, 0.8 is frequency.
    ## Here's the link to the textshaders documentation: https://renpy.org/doc/html/textshaders.html
    def wave_ts_tag(tag, argument, contents):
        return [  
                (renpy.TEXT_TAG, u"shader=wave:u__amplitude=20.0:u__frequency=0.8"),
        ] + contents + [
                (renpy.TEXT_TAG, u"/shader"),
        ]
    def shake_ts_tag(tag, argument, contents):
        return [
                
                (renpy.TEXT_TAG, u"shader=text_shake:u__strength=1.2"),
        ] + contents + [
                (renpy.TEXT_TAG, u"/shader"),
        ]

    def bigshake_ts_tag(tag, argument, contents):
        return [
                
                (renpy.TEXT_TAG, u"shader=text_shake:u__strength=2.0"),
        ] + contents + [
                (renpy.TEXT_TAG, u"/shader"),
        ]

    config.custom_text_tags["wave"] = wave_ts_tag
    config.custom_text_tags["shake"] = shake_ts_tag
    config.custom_text_tags["bigshake"] = bigshake_ts_tag