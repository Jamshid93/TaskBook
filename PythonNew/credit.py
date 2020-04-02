
# Deylik bir odam uy olmoqchi kreditga uni oldida yaxshi kredit ya'ni 10% va undan ko'ra sal qimmatroq kredit 20% kreditlar bor shu 
#   ko'rsatilgan foizlarda to'lashi kerak 
# Uyningnarxi=1000000 $ deylik
narx=1000000
juda_yaxshi_kredit=True

if juda_yaxshi_kredit:
    tolaydi=0.1*narx
else:
    tolaydi=0.2*narx

print(f"Uy uchun xar oy $ {tolaydi} to'laydi")