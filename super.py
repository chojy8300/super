#!/usr/bin/env python3
# Written by Jung Cho (jungyoun.cho@mmk.su.se), MMK, Stockholm University
import sys
import CifFile
import random


def read(cifName):
    a = []
    fileName = cifName+'.cif'
    my_cif = CifFile.CifFile(fileName)
    keys = my_cif.keys()
    strName = keys[0]
    cif = my_cif[strName]
    atmtype = cif['_atom_site_label']
    atmlabel = cif['_atom_site_type_symbol']
    xpos = cif['_atom_site_fract_x']
    ypos = cif['_atom_site_fract_y']
    zpos = cif['_atom_site_fract_z']
    iso = cif['_atom_site_U_iso_or_equiv']
    adp = cif['_atom_site_adp_type']
    occ = cif['_atom_site_occupancy']

    for i in range(len(atmtype)):
        a.append([atmtype[i], atmlabel[i], xpos[i], ypos[i], zpos[i], iso[i], adp[i], occ[i]])

    return a


def write_cif(cifName, ax, cx, fname):
    ary = read(cifName)
    f = open(fname, 'a')
    for i in range(len(ary)):
        for j in range(ax):
            for k in range(cx):
                print(ary[i][0], ary[i][1], float(ary[i][2])/ax+j/ax, ary[i][3], float(ary[i][4])/cx+k/cx, ary[i][5],
                      ary[i][6], ary[i][7], file=f)
    f.close()


def write_d5r(cifName, ax, cx, row, col, fname):
    ary = read(cifName)
    f = open(fname, 'a')
    for i in range(len(ary)):
        for j in range(row-1, row):
            for k in range(col-1, col):
                print(ary[i][0], ary[i][1], float(ary[i][2]) / ax + j / ax, ary[i][3], float(ary[i][4]) / cx + k / cx,
                      ary[i][5], ary[i][6], ary[i][7], file=f)
    f.close()


def randomize(flag, ax, cx, fname):
    f = open(fname, 'a')

    for i in range(ax):
        for j in range(cx):
            rn = random.uniform(0, 4)
            # print(rn)
            if flag == 'odd':
                if rn < 1:
                    write_d5r('odd_t1', ax, cx, i+1, j+1, fname)
                elif 1 <= rn < 2:
                    write_d5r('odd_t2', ax, cx, i+1, j+1, fname)
                elif 2 <= rn < 3:
                    write_d5r('odd_t3', ax, cx, i+1, j+1, fname)
                elif 3 <= rn < 4:
                    write_d5r('odd_t4', ax, cx, i+1, j+1, fname)
            elif flag == 'even':
                if rn < 1:
                    write_d5r('even_t1', ax, cx, i+1, j+1, fname)
                elif 1 <= rn < 2:
                    write_d5r('even_t2', ax, cx, i+1, j+1, fname)
                elif 2 <= rn < 3:
                    write_d5r('even_t3', ax, cx, i+1, j+1, fname)
                elif 3 <= rn < 4:
                    write_d5r('even_t4', ax, cx, i+1, j+1, fname)
    f.close()


def main():
    # super cell size
    ax = 20
    cx = 20

    # Lattice parameters
    a = 23.736
    b = 10.1738
    c = 21.323

    # Print fractional coordinates to the file
    f = open('mod.cif', 'w')
    print('data_meh\n_symmetry_space_group_name_H-M \'P1\'\n_symmetry_Int_Tables_number 1\n'
          '_symmetry_cell_setting triclinic\nloop_\n_symmetry_equiv_pos_as_xyz\nx,y,z\n'
          '_cell_length_a '+str(a*ax)+'\n_cell_length_b 10.1738\n_cell_length_c '
          + str(c*cx)+'\n_cell_angle_alpha 90\n'
          '_cell_angle_beta 111.83\n_cell_angle_gamma 90\nloop_\n_atom_site_label\n'
          '_atom_site_type_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n'
          '_atom_site_U_iso_or_equiv\n_atom_site_adp_type\n_atom_site_occupancy\n', file=f)
    f.close()
    write_cif('cas_odd', ax, cx, 'mod.cif')
    write_cif('cas_even', ax, cx, 'mod.cif')
    # # write_cif('odd_t1', ax, cx, 'mod.cif')
    # # write_cif('even_t2', ax, cx, 'mod.cif')
    # # randomize('odd', ax, cx, 'mod.cif')
    randomize('odd', ax, cx, 'mod.cif')
    randomize('even', ax, cx, 'mod.cif')


if __name__ == '__main__':
    main()
