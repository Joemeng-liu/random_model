import model

model_choti = model.one_model("model/chouti/urdf/chouti.urdf", 1, 0.32, 0.11, 0.111, z=0.10 + 0.625)

model_cube = model.one_model("model/cube1/urdf/cube1.urdf", 2, 0.036, 0.025, 0.025, z=0.0 + 0.625)
model_cube_r = model.one_model("model/cube1/urdf/cube1_r.urdf", 2, 0.035, 0.025, 0.025, z=0.0 + 0.625)
model_cube_g = model.one_model("model/cube1/urdf/cube1_g.urdf", 2, 0.035, 0.025, 0.025, z=0.0 + 0.625)
model_cube_b = model.one_model("model/cube1/urdf/cube1_b.urdf", 2, 0.035, 0.025, 0.025, z=0.0 + 0.625)

model_box = model.one_model("model/box/urdf/box.urdf", 3, 0.15, 0.145, 0.15, z=0.001 + 0.625)
model_box_r = model.one_model("model/box/urdf/box_r.urdf", 3, 0.145, 0.15, 0.15, z=0.001 + 0.625)
model_box_g = model.one_model("model/box/urdf/box_g.urdf", 3, 0.145, 0.15, 0.15, z=0.001 + 0.625)
model_box_b = model.one_model("model/box/urdf/box_b.urdf", 3, 0.145, 0.15, 0.15, z=0.001 + 0.625)

model_cover_box = model.one_model("model/cover_box/urdf/cover_box.urdf", 4, 0.13, 0.13, 0.13, z=0.0159 + 0.625)
model_cover_box_r = model.one_model("model/cover_box/urdf/cover_box_r.urdf", 4, 0.13, 0.13, 0.13, z=0.0159 + 0.625)
model_cover_box_g = model.one_model("model/cover_box/urdf/cover_box_g.urdf", 4, 0.13, 0.13, 0.13, z=0.0159 + 0.625)
model_cover_box_b = model.one_model("model/cover_box/urdf/cover_box_b.urdf", 4, 0.13, 0.13, 0.13, z=0.0159 + 0.625)

model_tray = model.one_model("model/tray/urdf/tray.urdf", 5, 0.33, 0.33, 0.33, z=0.0147 + 0.625)
model_tray_r = model.one_model("model/tray/urdf/tray_r.urdf", 5, 0.33, 0.33, 0.33, z=0.0147 + 0.625)
model_tray_g = model.one_model("model/tray/urdf/tray_g.urdf", 5, 0.33, 0.33, 0.33, z=0.0147 + 0.625)
model_tray_b = model.one_model("model/tray/urdf/tray_b.urdf", 5, 0.33, 0.33, 0.33, z=0.0147 + 0.625)

model_cup = model.one_model("model/cup_cy/urdf/cup_cy.urdf", 6, 0.085, 0.085, 0.085, z=0.038 + 0.625)
model_cup_r = model.one_model("model/cup_cy/urdf/cup_cy_r.urdf", 6, 0.085, 0.085, 0.085, z=0.038 + 0.625)
model_cup_g = model.one_model("model/cup_cy/urdf/cup_cy_g.urdf", 6, 0.085, 0.085, 0.085, z=0.038 + 0.625)
model_cup_b = model.one_model("model/cup_cy/urdf/cup_cy_b.urdf", 6, 0.085, 0.085, 0.085, z=0.038 + 0.625)

model_cup_cover = model.one_model("model/cup_cover/urdf/cup_cover.urdf", 7, 0.04, 0.04, 0.04, z=0.01 + 0.625)
model_cup_cover_r = model.one_model("model/cup_cover/urdf/cup_cover_r.urdf", 7, 0.04, 0.04, 0.04, z=0.01 + 0.625)
model_cup_cover_g = model.one_model("model/cup_cover/urdf/cup_cover_g.urdf", 7, 0.04, 0.04, 0.04, z=0.01 + 0.625)
model_cup_cover_b = model.one_model("model/cup_cover/urdf/cup_cover_b.urdf", 7, 0.04, 0.04, 0.04, z=0.01 + 0.625)

model_w_cup_w = model.one_model("model/w_cup/urdf/w_cup_w.urdf", 8, 0.09, 0.09, 0.09, z=0.085 + 0.625)
model_w_cup_r = model.one_model("model/w_cup/urdf/w_cup_r.urdf", 8, 0.09, 0.09, 0.09, z=0.085 + 0.625)
model_w_cup_g = model.one_model("model/w_cup/urdf/w_cup_g.urdf", 8, 0.09, 0.09, 0.09, z=0.085 + 0.625)
model_w_cup_b = model.one_model("model/w_cup/urdf/w_cup_b.urdf", 8, 0.09, 0.09, 0.09, z=0.085 + 0.625)

choti = [model_choti, model_choti, model_choti, model_choti]
cube = [model_cube,
        model_cube_r,
        model_cube_g,
        model_cube_b]
box = [model_box,
       model_box_r,
       model_box_g,
       model_box_b]
cover_box = [model_cover_box,
             model_cover_box_r,
             model_cover_box_g,
             model_cover_box_b]
tray = [model_tray,
        model_tray_r,
        model_tray_g,
        model_tray_b]
cup = [model_cup,
       model_cup_r,
       model_cup_g,
       model_cup_b]
cup_cover = [model_cup_cover,
             model_cup_cover_r,
             model_cup_cover_g,
             model_cup_cover_b]
w_cup = [model_w_cup_w,
         model_w_cup_r,
         model_w_cup_g,
         model_w_cup_b]

model_list = [choti, cube, box, cover_box, tray, cup, cup_cover, w_cup]
