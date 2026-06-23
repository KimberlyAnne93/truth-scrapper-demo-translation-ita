





















































































































































































































transform outline_transform(width=1, color="#fff", smoothing=1.0, end_color=None, num_passes=1, gradient_smoothing=None, is_mesh=True, mesh_pad=False, drawable_res=False, offset=(0, 0), smoothstep=True, power=None):


    shader 'feniks.outline'
    mesh is_mesh
    mesh_pad (False if not mesh_pad else (int(width),) * 4)
    gl_drawable_resolution drawable_res

    u_width float(width)
    u_num_passes ((max(float(num_passes), 1.0) if width > 0 else 1.0)
        if end_color is None or num_passes > 1 else float(width))
    u_line_color Color(color).rgba
    u_end_color Color(color if end_color is None else end_color).rgba
    u_has_gradient float(1.0 if end_color is not None else 0.0)
    u_smoothness (float(smoothing) if width > 0 else 1.0)
    u_gradient_smoothness (float(gradient_smoothing if gradient_smoothing is not None else smoothing) if width > 0 else 1.0)
    u_offset (float(offset[0]), float(offset[1]))
    u_smoothstep float(1.0 if end_color is not None and smoothstep else 0.0)
    u_power float(max(power, 0.0) if power is not None and end_color is not None else 0.0)




transform glow_outline(width=15, color="#fff", mesh_pad=False, num_passes=None, smoothstep=True, power=None):

    outline_transform(width, color, 20.0, "#0000", (num_passes or width*2.0),
        mesh_pad=mesh_pad, smoothstep=smoothstep, power=power)



transform drop_shadow(color="#0008", offset=(15, 15), mesh_pad=False):
    outline_transform(0, color, 1.0, mesh_pad=mesh_pad, offset=offset)




transform animated_demonstration():
    shader 'feniks.outline'
    mesh True mesh_pad (20, 20, 20, 20) gl_drawable_resolution False
    u_num_passes 3.0
    u_smoothness 2.0 u_gradient_smoothness 2.0
    u_has_gradient 0.0
    u_end_color Color("#f00").rgba
    u_power 0.0
    u_smoothstep 1.0

    block:
        parallel:
            u_line_color Color("#f00").rgba
            linear 0.5 u_line_color Color("#ff0").rgba
            linear 0.5 u_line_color Color("#0f0").rgba
            linear 0.5 u_line_color Color("#0ff").rgba
            linear 0.5 u_line_color Color("#00f").rgba
            linear 0.5 u_line_color Color("#f0f").rgba
            linear 0.5 u_line_color Color("#f00").rgba
            repeat
        parallel:
            u_width 1.0
            ease 2.0 u_width 6.0
            ease 2.0 u_width 1.0
            repeat
        parallel:
            u_offset (-10, 10)
            ease 1.0 u_offset (10, 10)
            ease 1.0 u_offset (10, -10)
            ease 1.0 u_offset (-10, -10)
            ease 1.0 u_offset (-10, 10)
            repeat






init -50 python:
    
    renpy.register_shader("feniks.outline", variables="""
        uniform float u_width;
        uniform vec4 u_line_color;
        uniform vec4 u_end_color;
        uniform float u_smoothness;
        uniform float u_gradient_smoothness;
        uniform float u_has_gradient;
        uniform float u_smoothstep;
        uniform float u_power;
        uniform float u_num_passes;
        uniform vec2 u_offset;

        uniform vec2 u_model_size;
        varying vec2 v_coords;
        varying vec2 v_size;
    """, vertex_300="""
        v_coords = vec2(a_position.x / u_model_size.x, a_position.y / u_model_size.y);
        v_size = u_model_size.xy;
    """, fragment_300="""
        float pi = 3.1415926535897932384626433832795;
        // We always check in at least 8 directions
        float angle_smooth = 8.0 * u_smoothness;
        float grad_smooth = 8.0 * u_gradient_smoothness;

        // Premultiply the alpha for the line colours (for mixing)
        vec4 line_color = vec4(u_line_color.rgb*u_line_color.a, u_line_color.a);
        vec4 end_color = vec4(u_end_color.rgb*u_end_color.a, u_end_color.a);

        // Figure out the size of one pixel based on the texture size
        vec2 pixel_size = vec2(1.0 / v_size.x, 1.0 / v_size.y);
        vec2 outline_offset = u_offset * pixel_size * vec2(-1.0);

        // Set up some initial values
        vec4 current_pixel = vec4(0.0);
        float closest_dist = u_width;
        vec4 og_color = texture2D(tex0, v_coords);
        float outline = 0.0;

        // This loop runs for num_passes, slowly getting larger and closer to
        // the final width number. The more passes, the better it handles
        // small pixel areas and sharp curves.
        for (float num=u_width; num>=0.0; num-=max(u_width/u_num_passes,
                min(pixel_size.x, pixel_size.y))) {
            // This loop runs for the number of angles the shader is
            // considering. The more angles, the rounder and smoother the
            // final outline.
            for (float i=0.0; i < angle_smooth; i++) {
                float angle = 2.0 * i * pi / angle_smooth;
                vec2 offset = vec2(cos(angle), sin(angle)) * num * pixel_size;
                current_pixel = texture2D(tex0, v_coords + offset + outline_offset);
                outline += current_pixel.a;
                // Also keep track of approximately how far this pixel is
                // from the main texture, for gradient purposes.
                if (current_pixel.a > 0.0) {
                    closest_dist = num;
                }
            }
        }
        // Make sure the outline doesn't go over 1.0; there can only be
        // 100% outline and 0% original image at most.
        outline = min(outline, 1.0);

        float closest = closest_dist/u_width;

        if (u_power > 0.0) {
            closest = max(min(pow(closest_dist/u_width, u_power), 1.0), 0.0);
        }
        // Smoothstep evens out the gradient a little towards the edges, so
        // the cutoff doesn't look so harsh.
        if (u_smoothstep > 0.0) {
            closest = smoothstep(0.0, 1.0, closest);
        }
        closest = min(u_has_gradient, closest);

        // Mix together the start/end line colours based on how far the pixel
        // is from the main image.
        vec4 blend_line = mix(line_color, end_color, closest);
        // And finally, mix the original image with the outline. This is so
        // the outline appears under translucent parts of the main image too,
        // where applicable.
        gl_FragColor = mix(og_color, blend_line, max(0.0, outline-og_color.a));
    """)


init python:
    build.classify("**outline_shader.rpy", None)
    build.classify("**outline_shader.rpyc", "archive")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
