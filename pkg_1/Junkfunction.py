def _setMatchData(self, days, n_match, k, teams):
    if k[1] == 0:
        self[days][n_match] = [int(k[0])]
    elif k[1] == 1:
        self[days][n_match] = [k[0]]
    elif k[1] == 2:
        self[days][n_match] = [k[0]]
    elif k[1] == 3:
        self[days][n_match] = [int(k[0])]
    elif k[1] == 4:
        self[days][n_match] = [int(k[0])]
    elif k[1] == 5:
        self[days][n_match] = [k[0]]
    elif k[1] == 6:
        self[days][n_match] = [int(k[0])]
    elif k[1] == 7:
        self[days][n_match] = [int(k[0])]
    elif k[1] == 8:
        self[days][n_match] += [k[0]]
        teams += 2
        # self._set_partialranking(days,n_match,nextday)
        # self._set_ranking(days,n_match, nextday)

    return teams

def _checkmatchpostponed(self, day, match):
    for i in range(len(self.teams) * 2 - 1, len(self) + 1):
        for k in self[i]:
            if self[i][k][9]:
                if self[i][k][0] < self[day][match][0]:
                    if self[i][k][5] == 'H':
                        t = 0
                        for elem in self[day]._ranking:
                            if elem[0] == self[i][k][1]:
                                elem[1] += 1
                                elem[2] += 3
                                self[day]._ranking[t] = elem
                            if elem[0] == self[i][k][2]:
                                elem[1] += 1
                                self[day]._ranking[t] = elem
                            t += 1
                        self[i][k][9] = False
                    elif self[day][match][5] == 'D':
                        t = 0
                        for elem in self[day]._ranking:
                            if elem[0] == self[i][k][1]:
                                elem[1] += 1
                                elem[2] += 1
                                self[day]._ranking[t] = elem
                            if elem[0] == self[i][k][2]:
                                elem[1] += 1
                                elem[2] += 1
                                self[day]._ranking[t] = elem
                            t += 1
                        self[i][k][9] = False
                    else:
                        t = 0
                        for elem in self[day]._ranking:
                            if elem[0] == self[i][k][1]:
                                elem[1] += 1
                                self[day]._ranking[t] = elem
                            if elem[0] == self[i][k][2]:
                                elem[1] += 1
                                elem[2] += 3
                                self[day]._ranking[t] = elem
                            t += 1
                        self[i][k][9] = False
                else:
                    return
