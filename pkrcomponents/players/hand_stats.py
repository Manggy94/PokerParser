from attrs import define, field, Factory
from attrs.validators import instance_of, ge, optional

from pkrcomponents.actions.actions_sequence import ActionsSequence
from pkrcomponents.cards.combo import Combo

@define
class HandStats:
    """
    This class represents the statistics of a player's hand in a poker game
    Attributes:
        # A. Preflop stats
        # 1. Flags
        flag_vpip (bool): Whether the player voluntarily put money in the pot
        flag_preflop_open_opportunity (bool): Whether the player had the opportunity to open preflop
        flag_preflop_opened (bool): Whether the player opened preflop
        flag_preflop_first_raise (bool): Whether the player made the first raise preflop
        flag_preflop_fold (bool): Whether the player folded preflop
        flag_preflop_limp (bool): Whether the player limped preflop
        flag_preflop_cold_called (bool): Whether the player cold called preflop
        flag_preflop_face_raise (bool): Whether the player faced a raise preflop
        flag_preflop_bet (bool): Whether the player bet preflop (Realized at least one raise)
        flag_preflop_3bet_opportunity (bool): Whether the player had the opportunity to 3bet preflop
        flag_preflop_3bet (bool): Whether the player 3bet preflop
        flag_preflop_face_3bet (bool): Whether the player faced a 3bet preflop
        flag_preflop_4bet_opportunity (bool): Whether the player had the opportunity to 4+bet preflop
        flag_preflop_4bet (bool): Whether the player 4+bet preflop
        flag_preflop_face_4bet (bool): Whether the player faced a 4+bet preflop
        flag_preflop_squeeze_opportunity (bool): Whether the player had the opportunity to squeeze preflop
        flag_preflop_squeeze (bool): Whether the player squeezed preflop
        # 2. Counts
        count_preflop_player_raises (int): The number of raises the player made preflop
        count_preflop_player_calls (int): The number of calls the player made preflop
        count_faced_limps (int): The number of limps the player faced preflop
        # 3. Sequences
        preflop_actions_sequence (ActionsSequence): The sequence of actions the player made preflop
        # B. Flop stats
        # 1. Flags
        flag_flop_bet (bool): Whether the player bet on the flop
        flag_flop_open_opportunity (bool): Whether the player had the opportunity to open on the flop
        flag_flop_open (bool): Whether the player opened on the flop
        flag_flop_cbet_opportunity (bool): Whether the player had the opportunity to make a continuation bet on the flop
        flag_flop_cbet (bool): Whether the player made a continuation bet on the flop
        flag_flop_donk_bet_opportunity (bool): Whether the player had the opportunity to make a donk bet on the flop
        flag_flop_donk_bet (bool): Whether the player made a donk bet on the flop
        flag_flop_first_raise (bool): Whether the player made the first raise on the flop
        flag_flop_check (bool): Whether the player checked on the flop
        flag_flop_3bet_opportunity (bool): Whether the player had the opportunity to 3bet on the flop
        flag_flop_3bet (bool): Whether the player 3bet on the flop
        flag_flop_4bet_opportunity (bool): Whether the player had the opportunity to 4+bet on the flop
        flag_flop_4bet (bool): Whether the player 4+bet on the flop
        # 2. Counts
        # 3. Sequences
        # C. Turn stats
        # 1. Flags
        # 2. Counts
        # 3. Sequences
        # D. River stats
        # 1. Flags
        # 2. Counts
        # 3. Sequences
        # E. General stats
    """
    # pylint: disable=too-many-instance-attributes
    # A. Preflop stats
    # 1. Flags
    flag_vpip = field(default=False, validator=instance_of(bool))
    flag_preflop_open_opportunity = field(default=False, validator=instance_of(bool))
    flag_preflop_opened = field(default=False, validator=instance_of(bool))
    flag_preflop_first_raise = field(default=False, validator=instance_of(bool))
    flag_preflop_fold = field(default=False, validator=instance_of(bool))
    flag_preflop_limp = field(default=False, validator=instance_of(bool))
    flag_preflop_cold_called = field(default=False, validator=instance_of(bool))
    flag_preflop_face_raise = field(default=False, validator=instance_of(bool))
    flag_preflop_bet = field(default=False, validator=instance_of(bool))
    flag_preflop_3bet_opportunity = field(default=False, validator=instance_of(bool))
    flag_preflop_3bet = field(default=False, validator=instance_of(bool))
    flag_preflop_face_3bet = field(default=False, validator=instance_of(bool))
    flag_preflop_4bet_opportunity = field(default=False, validator=instance_of(bool))
    flag_preflop_4bet = field(default=False, validator=instance_of(bool))
    flag_preflop_face_4bet = field(default=False, validator=instance_of(bool))
    flag_preflop_squeeze_opportunity = field(default=False, validator=instance_of(bool))
    flag_preflop_squeeze = field(default=False, validator=instance_of(bool))
    flag_preflop_face_squeeze = field(default=False, validator=instance_of(bool))
    # 2. Counts
    count_preflop_player_raises = field(default=0, validator=ge(0))
    count_preflop_player_calls = field(default=0, validator=ge(0))
    count_faced_limps = field(default=0, validator=ge(0))
    # 3. Sequences
    preflop_actions_sequence = field(default=Factory(lambda: ActionsSequence()), validator=instance_of(ActionsSequence))
    # B. Flop stats
    # 1. Flags
    flag_flop_bet = field(default=False, validator=instance_of(bool))
    flag_flop_open_opportunity = field(default=False, validator=instance_of(bool))
    flag_flop_open = field(default=False, validator=instance_of(bool))
    flag_flop_cbet_opportunity = field(default=False, validator=instance_of(bool))
    flag_flop_cbet = field(default=False, validator=instance_of(bool))
    flag_flop_donk_bet_opportunity = field(default=False, validator=instance_of(bool))
    flag_flop_donk_bet = field(default=False, validator=instance_of(bool))
    flag_flop_first_raise = field(default=False, validator=instance_of(bool))
    flag_flop_check = field(default=False, validator=instance_of(bool))
    flag_flop_3bet_opportunity = field(default=False, validator=instance_of(bool))
    flag_flop_3bet = field(default=False, validator=instance_of(bool))
    flag_flop_4bet_opportunity = field(default=False, validator=instance_of(bool))
    flag_flop_4bet = field(default=False, validator=instance_of(bool))
    # 2. Counts
    # 3. Sequences
    flop_actions_sequence = field(default=Factory(lambda: ActionsSequence()), validator=instance_of(ActionsSequence))
    # C. Turn stats
    # 1. Flags
    flag_turn_bet = field(default=False, validator=instance_of(bool))
    flag_turn_check = field(default=False, validator=instance_of(bool))
    # 2. Counts
    # D. River stats
    # 1. Flags
    flag_river_bet = field(default=False, validator=instance_of(bool))
    flag_river_check = field(default=False, validator=instance_of(bool))
    # 2. Counts
    # E. General stats
    combo = field(default=None, validator=optional(instance_of(Combo)))
    went_to_showdown = field(default=False, validator=instance_of(bool))

    def reset(self):
        """
        Resets the statistics
        """
        # A. Preflop stats
        # 1. Flags
        self.flag_vpip = False
        self.flag_preflop_open_opportunity = False
        self.flag_preflop_opened = False
        self.flag_preflop_first_raise = False
        self.flag_preflop_fold = False
        self.flag_preflop_limp = False
        self.flag_preflop_cold_called = False
        self.flag_preflop_face_raise = False
        self.flag_preflop_bet = False
        self.flag_preflop_3bet_opportunity = False
        self.flag_preflop_3bet = False
        self.flag_preflop_face_3bet = False
        self.flag_preflop_4bet_opportunity = False
        self.flag_preflop_4bet = False
        self.flag_preflop_face_4bet = False
        self.flag_preflop_squeeze_opportunity = False
        self.flag_preflop_squeeze = False
        # 2. Counts
        self.count_preflop_player_raises = 0
        self.count_preflop_player_calls = 0
        self.count_faced_limps = 0
        # 3. Sequences
        self.preflop_actions_sequence = ActionsSequence()
        # B. Flop stats
        # 1. Flags
        self.flag_flop_bet = False
        self.flag_flop_cbet_opportunity = False
        self.flag_flop_cbet = False
        self.flag_flop_first_raise = False
        self.flag_flop_check = False
        self.flag_flop_3bet_opportunity = False
        self.flag_flop_3bet = False
        self.flag_flop_4bet_opportunity = False
        self.flag_flop_4bet = False
        # 2. Counts
        # 3. Sequences
        self.flop_actions_sequence = ActionsSequence()
        # C. Turn stats



