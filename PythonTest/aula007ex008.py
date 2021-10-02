m = float(input('Digite medida em metros: '))
cm = m * 100
mm = m * 1000
dm = m / 10
hm = m / 100
km = m / 1000
print('A medida {}m corresponde a {}cm, {}mm, {}dm, {}hm e {}km '.format(m, cm, mm, dm, hm, km))
print('A medida corresponde a {} m, {} mm, {} dm, {} hm, {} km '
      . format(m * 100, m * 100, m / 10, m / 10, m / 100, m / 1000.))
