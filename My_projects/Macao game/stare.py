# def shuffle_cards(self):
#     shuffled_keys = list(self.card_images.keys())
#     random.shuffle(shuffled_keys)

#     # our shuffled cards
#     self.shuffled_card_images = {
#         key: self.card_images[key] for key in shuffled_keys}

#     return self.shuffled_card_images

# def draw_card(self, x, y):
#     screen.blit(self.image, (x, y))

# # the black hearts
# self.two_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/H2.png").convert_alpha()
# self.three_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/H3.png").convert_alpha()
# self.four_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/H4.png").convert_alpha()
# self.five_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/H5.png").convert_alpha()
# self.six_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/H6.png").convert_alpha()
# self.seven_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/H7.png").convert_alpha()
# self.eight_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/H8.png").convert_alpha()
# self.nine_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/H9.png").convert_alpha()
# self.ten_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/H10.png").convert_alpha()
# self.jupek_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/HJ.png").convert_alpha()
# self.queen_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/HQ.png").convert_alpha()
# self.king_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/HK.png").convert_alpha()
# self.as_black_hearts = pygame.image.load(
#     "Cards_graphic/BLack Hearts/HA.png").convert_alpha()

# # the clubs
# self.two_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/C2.png").convert_alpha()
# self.three_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/C3.png").convert_alpha()
# self.four_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/C4.png").convert_alpha()
# self.five_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/C5.png").convert_alpha()
# self.six_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/C6.png").convert_alpha()
# self.seven_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/C7.png").convert_alpha()
# self.eight_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/C8.png").convert_alpha()
# self.nine_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/C9.png").convert_alpha()
# self.ten_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/C10.png").convert_alpha()
# self.jupek_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/CJ.png").convert_alpha()
# self.queen_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/CQ.png").convert_alpha()
# self.king_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/CK.png").convert_alpha()
# self.as_clubs = pygame.image.load(
#     "Cards_graphic/Clubs/CA.png").convert_alpha()

# # the diamonds
# self.two_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/D2.png").convert_alpha()
# self.three_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/D3.png").convert_alpha()
# self.four_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/D4.png").convert_alpha()
# self.five_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/D5.png").convert_alpha()
# self.six_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/D6.png").convert_alpha()
# self.seven_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/D7.png").convert_alpha()
# self.eight_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/D8.png").convert_alpha()
# self.nine_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/D9.png").convert_alpha()
# self.ten_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/D10.png").convert_alpha()
# self.jupek_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/DJ.png").convert_alpha()
# self.queen_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/DQ.png").convert_alpha()
# self.king_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/DK.png").convert_alpha()
# self.as_diamonds = pygame.image.load(
#     "Cards_graphic/Diamonds/DA.png").convert_alpha()

# # the red hearts
# self.two_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/H2.png").convert_alpha()
# self.three_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/H3.png").convert_alpha()
# self.four_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/H4.png").convert_alpha()
# self.five_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/H5.png").convert_alpha()
# self.six_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/H6.png").convert_alpha()
# self.seven_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/H7.png").convert_alpha()
# self.eight_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/H8.png").convert_alpha()
# self.nine_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/H9.png").convert_alpha()
# self.ten_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/H10.png").convert_alpha()
# self.jupek_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/HJ.png").convert_alpha()
# self.queen_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/HQ.png").convert_alpha()
# self.king_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/HK.png").convert_alpha()
# self.as_red_hearts = pygame.image.load(
#     "Cards_graphic/Red Hearts/HA.png").convert_alpha()

# self.card_images = {
#     '2_black_hearts': self.two_black_hearts,
#     '3_black_hearts': self.three_black_hearts,
#     '4_black_hearts': self.four_black_hearts,
#     '5_black_hearts': self.five_black_hearts,
#     '6_black_hearts': self.six_black_hearts,
#     '7_black_hearts': self.seven_black_hearts,
#     '8_black_hearts': self.eight_black_hearts,
#     '9_black_hearts': self.nine_black_hearts,
#     '10_black_hearts': self.ten_black_hearts,
#     'J_black_hearts': self.jupek_black_hearts,
#     'Q_black_hearts': self.queen_black_hearts,
#     'K_black_hearts': self.king_black_hearts,
#     'AS_black_hearts': self.as_black_hearts,
#     '2_clubs': self.two_clubs,
#     '3_clubs': self.three_clubs,
#     '4_clubs': self.four_clubs,
#     '5_clubs': self.five_clubs,
#     '6_clubs': self.six_clubs,
#     '7_clubs': self.seven_clubs,
#     '8_clubs': self.eight_clubs,
#     '9_clubs': self.nine_clubs,
#     '10_clubs': self.ten_clubs,
#     'J_clubs': self.jupek_clubs,
#     'Q_clubs': self.queen_clubs,
#     'K_clubs': self.king_clubs,
#     'AS_clubs': self.as_clubs,
#     '2_diamonds': self.two_diamonds,
#     '3_diamonds': self.three_diamonds,
#     '4_diamonds': self.four_diamonds,
#     '5_diamonds': self.five_diamonds,
#     '6_diamonds': self.six_diamonds,
#     '7_diamonds': self.seven_diamonds,
#     '8_diamonds': self.eight_diamonds,
#     '9_diamonds': self.nine_diamonds,
#     '10_diamonds': self.ten_diamonds,
#     'J_diamonds': self.jupek_diamonds,
#     'Q_diamonds': self.queen_diamonds,
#     'K_diamonds': self.king_diamonds,
#     'AS_diamonds': self.as_diamonds,
#     '2_red_hearts': self.two_red_hearts,
#     '3_red_hearts': self.three_red_hearts,
#     '4_red_hearts': self.four_red_hearts,
#     '5_red_hearts': self.five_red_hearts,
#     '6_red_hearts': self.six_red_hearts,
#     '7_red_hearts': self.seven_red_hearts,
#     '8_red_hearts': self.eight_red_hearts,
#     '9_red_hearts': self.nine_red_hearts,
#     '10_red_hearts': self.ten_red_hearts,
#     'J_red_hearts': self.jupek_red_hearts,
#     'Q_red_hearts': self.queen_red_hearts,
#     'K_red_hearts': self.king_red_hearts,
#     'AS_red_hearts': self.as_red_hearts
# }
