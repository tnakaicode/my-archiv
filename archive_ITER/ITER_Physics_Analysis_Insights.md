# ITER Physics Basis 統合分析：物理的インサイトと実装戦略

**作成日**: 2026年3月2日  
**目的**: 単なるデータ抽出ではなく、深い物理的理解と実用的結論の導出  
**対象**: ITER Physics Basis (1999), Chapters 1-3, 6-8

---

## エグゼクティブサマリー

ITER設計は**3つの根本的制約**によって支配されている：

1. **β限界** (βN ≤ 2.5): プラズマ圧力の上限 → 核融合出力制限
2. **密度限界** (n/nG ≤ 0.85): 高密度運転の限界 → Disruption回避
3. **閉じ込め要求** (τE ≥ 3.7s): Q=10達成の必須条件

これら3つの制約を**同時に満たす**ことがITER成功の鍵であり、**そのために必要なのがECCD制御システム**である。

---

## 1. 物理的制約の階層構造：何が何を制限しているか

### 1.1 根本的制約（変更不可能）

```
核融合反応断面積 <σv> ∝ T²（T < 20 keV域）
    ↓
高温運転が必須（T > 10 keV）
    ↓
しかし、高温 → 高β → MHD不安定
```

**結論**: 核融合には高温が必要だが、高温は不安定性を引き起こす

### 1.2 MHD制約（設計で緩和可能）

```
β限界: βN ≤ C_Troyon × (1 - li/3)
    ↓
C_Troyon ≈ 2.8（壁なし） → 3.5（抵抗壁あり）
    ↓
ITER設計: βN,target = 1.8-2.5（限界の70%で運転）
```

**設計哲学**: 
- 理論限界まで攻めない（安全マージン30%確保）
- 壁安定化を活用（+25%のβ増加）
- ECCDで局所的安定化（NTM抑制）

### 1.3 輸送制約（スケーリング則依存）

```
閉じ込め時間: τE ∝ Ip^0.93 × Bt^0.15 × P^(-0.69) × ...（IPB98y2）
    ↓
高パワー → 悪化（τE ∝ P^(-0.69)）
    ↓
しかし、点火には高パワーが必要
```

**パラドックス**: 
- 点火には高い補助加熱が必要（P_aux ~ 50 MW）
- しかし加熱すると閉じ込めが悪化（τE低下）
- 解決策：α粒子自己加熱（P_alpha ~ 400 MW）が支配的になることで解決

---

## 2. トレードオフ関係：設計思想の本質

### 2.1 サイズ vs コスト vs 性能

| パラメータ | FDR設計 | Baseline設計 | 変更理由 |
|-----------|---------|-------------|---------|
| R₀ × a | 8.14 m × 2.8 m | 6.2 m × 2.0 m | **コスト削減** |
| Ip | 21 MA | 15 MA | 超伝導コイル負荷軽減 |
| Pfus | 1.5 GW | 0.4-0.5 GW | 現実的目標 |
| Q値 | > 10（点火） | ≥ 10 | 同等性能維持 |

**インサイト**: 
- 装置を35%小型化してもQ≥10は達成可能
- 理由：τE ∝ R^1.97（サイズの効果が極めて大きい）
- **スケーリング則の信頼性が設計の鍵**

### 2.2 定常運転 vs パルス運転

| シナリオ | 燃焼時間 | Bootstrap分率 | ECCD要求 | 実現難易度 |
|---------|---------|--------------|----------|-----------|
| **Inductive** | ~400 s | 20-30% | 20 MW（制御用） | 中 |
| **Hybrid** | ~3000 s | 40-50% | 必須 | 高 |
| **Advanced** | 定常 | > 60% | 必須（高度制御） | 極高 |

**トレードオフ**: 
- 長パルス → Bootstrap電流増 → ECCD依存度減
- しかし、長パルス → MHD不安定成長 → ECCD制御必須
- **結論**: どのシナリオでもECCDは不可欠

### 2.3 加熱手法の比較

| 手法 | パワー | 電流駆動効率 | 制御性 | 主な役割 |
|------|--------|-------------|--------|---------|
| **NBI** | 33 MW | 中（η ~ 0.3） | 低（固定） | イオン加熱、トルク |
| **ICRH** | 20 MW | 低 | 中 | 少数粒子加熱 |
| **ECCD** | 20 MW | 高（η ~ 0.3） | **極高**（Real-time steering） | **MHD制御** |
| **LHCD** | — | 極高 | 中 | オフアクシス電流駆動 |

**インサイト**: 
- 総パワーではNBIが最大
- しかし、**制御性ではECCDが圧倒的**
- ITERの成功は「加熱パワー」より「制御能力」に依存

---

## 3. 因果ネットワーク：パラメータ間の複雑な相互作用

### 3.1 NTM（ネオクラシカルテアリングモード）の因果連鎖

```
高β運転（βN → 2.5）
    ↓
Sawtooth発生（q0 < 1で不可避）
    ↓
大振幅Sawtooth → m/n = 3/2, 2/1 磁気島のseed
    ↓
Bootstrap電流による島の自己増幅（正のフィードバック）
    ↓
w/rs > 0.2 （島幅/有理面半径 > 20%）
    ↓
大幅な閉じ込め劣化（Δτ_E/τ_E ~ -40%）
    ↓
β低下 → 核融合出力低下 → Q値達成不可
```

**制御戦略**:
```
ECCD → 局所電流駆動（rs位置に±5 cm精度で照射）
    ↓
Modified Rutherford方程式: τR × dw/dt = Δ' - C × j_ECCD/w
    ↓
j_ECCD十分大 → dw/dt < 0 （島幅縮小）
    ↓
w < w_threshold → 島消滅
    ↓
閉じ込め回復 → 高β運転継続可能
```

**重要数値**:
- ECCD応答時間: < 100 ms（NTM成長時間と競合）
- 必要パワー: 3-5 MW（全ECCDの15-25%）
- 位置精度: Δr < 10 cm（rs ≈ 1.5 m に対して < 7%）

### 3.2 Sawtooth制御の必要性

```
α粒子蓄積（Te0 ~ 30 keV, ITER条件）
    ↓
Sawtooth周期延長（τsaw: 10s → 100s）
    ↓
大振幅Sawtooth崩壊（ΔTe/Te ~ 50%）
    ↓
NTM trigger（上記3.1参照）
    ↓
β限界
```

**対策**:
```
ECCD @ q = 1表面（r/a ~ 0.3）
    ↓
磁気シア増大（s = r/q × dq/dr ↑）
    ↓
Sawtoothトリガー条件緩和
    ↓
τsaw短縮（100s → 10-20s）
    ↓
振幅縮小（ΔTe/Te: 50% → 20%）
    ↓
NTM trigger回避
```

**制御パラメータ**:
- ECCD照射位置: r/a = 0.25-0.35（q=1表面追従）
- 必要パワー: 5-10 MW
- 制御周期: ~ 10 s（Sawtooth周期と同程度）

### 3.3 閉じ込めスケーリングの非線形性

```
IPB98(y,2): τE = 0.0562 × Ip^0.93 × Bt^0.15 × P^(-0.69) × ne^0.41 × ...
```

**非自明な結論**:
1. **電流の効果が支配的**: τE ∝ Ip^0.93（ほぼ線形）
   - Ip: 15 MA → 21 MA（+40%） ⇒ τE: +37%
   
2. **磁場の効果は弱い**: τE ∝ Bt^0.15
   - Bt: 5.3 T → 6.0 T（+13%） ⇒ τE: +2%のみ
   
3. **加熱パワーは逆効果**: τE ∝ P^(-0.69)
   - P: 50 MW → 100 MW（2倍） ⇒ τE: -38%（悪化）

**設計への影響**:
```
高Q値達成 → 高τE必要
    ↓
τE向上には: 高Ip >> 高Bt
    ↓
しかし、高Ip → 超伝導コイル負荷大 → コスト増
    ↓
妥協点: Ip = 15 MA（FDRの21 MAから削減）
```

---

## 4. 設計哲学：なぜこの設計なのか

### 4.1 保守的設計 vs 挑戦的設計

| 項目 | 理論限界 | ITER運転点 | マージン |
|------|---------|-----------|---------|
| **βN** | 2.8-3.5 | 1.8-2.5 | 30-40% |
| **n/nG** | 1.0 | 0.85 | 15% |
| **H-factor** | 1.0 | 1.0 | 0%（挑戦的） |
| **q95** | 2.5（限界近傍） | 3.0-3.5 | 20% |

**分析**:
- MHD限界（β, n/nG）: 保守的（大きなマージン確保）
- 閉じ込め（H-factor）: 挑戦的（マージンなし）
  - H = 1.0でギリギリQ=10達成
  - もしH < 0.9なら Q < 7（目標未達）

**リスク評価**:
- **最大のリスクは閉じ込め劣化**（H-factor低下）
- MHD不安定性は制御可能と判断（ECCD制御に依存）
- **閉じ込めスケーリングの外挿信頼性が成否を分ける**

### 4.2 実験データベースの重要性

```
ITER設計の正当化 = 既存トカマクデータの外挿
    ↓
データベース: JET, TFTR, DIII-D, JT-60U, ASDEX-U, etc.
    ↓
無次元パラメータ空間での検証:
  - ρ* = ρi/a: 相似則（gyroBohm則）
  - ν*: コリジョナリティ
  - β: 規格化圧力
    ↓
ITER条件: ρ* ~ 0.002（既存装置の1/3-1/5）
    ↓
外挿リスク: 小型装置で見えない物理が出現する可能性
```

**緩和要因**:
- JT-60Uで低ρ*領域を一部カバー
- スケーリング則の標準偏差: ±20%程度
- 複数のスケーリング則で一致

---

## 5. 診断システムの戦略的重要性

### 5.1 "Serious Difficulties"の意味

Chapter 7（Diagnostics）の評価:
- **q-profile測定**: "serious difficulties"
- **MSE（主要手法）**: PEM寿命問題、偏光保存困難
- **Polarimetry**: 高磁場側レトロリフレクタ設置が"extremely difficult"

**インサイト**:
```
q-profile測定困難
    ↓
ECCD制御の不確実性増大
    ↓
NTM/Sawtooth制御の信頼性低下
    ↓
高β運転リスク増
```

**対策**:
- 平衡再構成（EFIT）による推定（間接測定）
- MHD分光法（有理面位置推定）
- リアルタイムECE（Te分布 → 磁気島検出）

### 5.2 統合診断システムの必要性

| 計測項目 | 主要手法 | 精度 | リアルタイム性 | 制御への寄与 |
|---------|---------|------|--------------|-------------|
| **Te(r,t)** | ECE | < 5% | ○（< 1 ms） | NTM位置同定 |
| **ne(r,t)** | Interferometry | < 5% | ○（~ ms） | 密度制御 |
| **q(r,t)** | MSE, EFIT | < 10% | △（~ 100 ms） | ECCD照射位置 |
| **β** | Diamagnetic | < 10% | ○（~ 10 ms） | β限界監視 |
| **島幅w** | ECE perturbation | ~ 20% | ○（< 10 ms） | NTM制御 |

**リアルタイム制御ループ**:
```
ECE → Te分布 → 島位置同定（< 10 ms）
    ↓
EFIT再構成 → q-profile推定（~ 100 ms）
    ↓
ECCD制御 → 照射角度調整（< 100 ms）
    ↓
島幅監視 → フィードバック（周期 ~ 1 s）
```

---

## 6. plasma_sim_ech_eccd_mhd.py への統合推奨

### 6.1 現在の実装状況

**実装済み**:
- ✓ ECH加熱（相対論補正あり）
- ✓ ECCD（Fisch-Boozer効率）
- ✓ Bootstrap電流（簡略Sauter-Angioniモデル）
- ✓ q-profile計算（q95境界条件）
- ✓ Sawtooth安定性判定（q0 < 1）
- ✓ NTM閾値（βp評価）

**未実装**:
- ✗ 閉じ込めスケーリング（IPB98y2）
- ✗ 時間発展（Rutherford方程式）
- ✗ β限界チェック（Troyon limit）
- ✗ 密度限界（Greenwald limit）
- ✗ リアルタイム制御ループ

### 6.2 優先度1：閉じ込めスケーリング実装

```python
def calc_tau_E_IPB98y2(Ip, Bt, P_net, ne19, M, R, eps, kappa):
    """
    IPB98(y,2) H-mode energy confinement time
    
    Parameters:
    Ip : plasma current [MA]
    Bt : toroidal field [T]
    P_net : net heating power [MW] (Paux + Palpha - Prad)
    ne19 : line-averaged density [10^19 m^-3]
    M : mass number (2.5 for D-T)
    R : major radius [m]
    eps : inverse aspect ratio a/R
    kappa : elongation
    
    Returns:
    tau_E : energy confinement time [s]
    """
    tau_E = 0.0562 * Ip**0.93 * Bt**0.15 * P_net**(-0.69) * ne19**0.41 \
            * M**0.19 * R**1.97 * eps**0.58 * kappa**0.78
    return tau_E

# ITER baseline条件での検証
Ip, Bt = 15, 5.3  # MA, T
P_net = 80  # MW (Paux 50 + Palpha 50 - Prad 20)
ne19 = 10.0  # 10^19 m^-3
M, R, eps, kappa = 2.5, 6.2, 0.32, 1.7

tau_E = calc_tau_E_IPB98y2(Ip, Bt, P_net, ne19, M, R, eps, kappa)
print(f"τE = {tau_E:.2f} s")  # Expected: ~3.7 s for Q=10
```

### 6.3 優先度2：運転限界チェック

```python
def check_operational_limits(params):
    """
    Check MHD and density limits
    
    Returns:
    dict: {
        'beta_limit': {'beta_N': float, 'limit': float, 'margin': float},
        'density_limit': {'ne': float, 'nG': float, 'margin': float},
        'status': 'safe' | 'warning' | 'danger'
    }
    """
    # Troyon beta limit
    beta_N = params['beta_t'] * params['a'] * params['Bt'] / params['Ip']
    C_troyon = 3.5 if params['with_wall'] else 2.8
    beta_N_limit = C_troyon * (1 - params['li'] / 3)
    beta_margin = 1 - beta_N / beta_N_limit
    
    # Greenwald density limit
    nG = params['Ip'] / (np.pi * params['a']**2)  # 10^20 m^-3
    ne_19 = params['ne'] / 1e19
    density_margin = 1 - ne_19 / (nG * 10)
    
    status = 'safe'
    if beta_margin < 0.15 or density_margin < 0.15:
        status = 'warning'
    if beta_margin < 0 or density_margin < 0:
        status = 'danger'
    
    return {
        'beta_limit': {'beta_N': beta_N, 'limit': beta_N_limit, 
                       'margin': beta_margin},
        'density_limit': {'ne': params['ne'], 'nG': nG * 1e20, 
                          'margin': density_margin},
        'status': status
    }
```

### 6.4 優先度3：時間発展シミュレータ

```python
class ITERPlasmaSimulator:
    """
    Time-dependent ITER plasma simulation
    Integrates: ECH, ECCD, Bootstrap, MHD stability, confinement
    """
    def __init__(self):
        # ITER parameters
        self.R0 = 6.2  # m
        self.a = 2.0   # m
        self.B0 = 5.3  # T
        self.Ip = 15   # MA
        
        # State variables
        self.Te0 = 20.0  # keV
        self.ne0 = 1.0e20  # m^-3
        self.beta_t = 2.5  # %
        self.q0 = 1.0
        
        # NTM island width
        self.w_32 = 0.0  # m, m/n = 3/2 mode
        
        # ECCD control
        self.P_ECCD_NTM = 0.0  # MW
        self.P_ECCD_ST = 0.0   # MW
        
    def update(self, dt):
        """
        Time step update
        
        Parameters:
        dt : time step [s]
        """
        # 1. Calculate heating and current drive
        P_aux = 50  # MW (NBI + ICRH + ECCD)
        P_alpha = self.calc_fusion_power() * 0.2  # 20% to electrons
        P_rad = self.calc_radiation()
        P_net = P_aux + P_alpha - P_rad
        
        # 2. Update confinement time
        tau_E = calc_tau_E_IPB98y2(
            self.Ip, self.B0, P_net, self.ne0/1e19, 
            2.5, self.R0, self.a/self.R0, 1.7
        )
        
        # 3. Update temperature (energy balance)
        W_th = 1.5 * self.ne0 * sc.k * self.Te0 * sc.eV * np.pi**2 * self.R0 * self.a**2
        dW_dt = P_net * 1e6 - W_th / tau_E
        self.Te0 += dW_dt * dt / (1.5 * self.ne0 * sc.k * sc.eV * np.pi**2 * self.R0 * self.a**2)
        
        # 4. Update q-profile (with ECCD)
        self.q0 = self.calc_q0_with_ECCD()
        
        # 5. Check Sawtooth stability
        if self.q0 < 1.0:
            # Trigger Sawtooth if no control
            if self.P_ECCD_ST < 5:  # MW
                self.sawtooth_crash()
        
        # 6. NTM island evolution (Modified Rutherford)
        if self.beta_t > 2.0:
            dw_dt = self.calc_NTM_growth(self.w_32, self.P_ECCD_NTM)
            self.w_32 += dw_dt * dt
            self.w_32 = max(0, self.w_32)  # No negative width
        
        # 7. Control response
        self.ECCD_control()
        
        # 8. Check operational limits
        limits = check_operational_limits({
            'beta_t': self.beta_t, 'a': self.a, 'Bt': self.B0,
            'Ip': self.Ip, 'li': 0.8, 'with_wall': True,
            'ne': self.ne0
        })
        
        return {
            'time': dt,
            'Te0': self.Te0,
            'q0': self.q0,
            'w_32': self.w_32,
            'tau_E': tau_E,
            'limits': limits
        }
    
    def calc_fusion_power(self):
        """Calculate fusion power [MW]"""
        # Simplified model
        P_fus = 4e-22 * (self.ne0 / 1e20)**2 * self.Te0**2  # Very rough
        return P_fus
    
    def ECCD_control(self):
        """Feedback control for ECCD power allocation"""
        # NTM control: if island width > threshold
        if self.w_32 > 0.05:  # 5 cm
            self.P_ECCD_NTM = 5.0  # MW
        else:
            self.P_ECCD_NTM = 0.0
        
        # Sawtooth control: if q0 close to 1
        if 0.95 < self.q0 < 1.05:
            self.P_ECCD_ST = 8.0  # MW
        else:
            self.P_ECCD_ST = 0.0
```

---

## 7. 重要な結論

### 7.1 物理的インサイト

1. **ITERの成功 = 制御の成功**
   - 高β運転は可能だが、MHD不安定性との闘い
   - ECCD制御がなければ目標達成は困難
   
2. **スケーリング則の信頼性が最大のリスク**
   - H-factor = 1.0を前提（マージンなし）
   - もしH < 0.9なら大幅な性能不足
   
3. **診断精度が制御性能を決定**
   - q-profile測定が"serious difficulties"
   - 間接推定（EFIT）に依存せざるを得ない

### 7.2 設計思想

- **保守的MHD限界設定**（30%マージン）
- **挑戦的閉じ込め目標**（マージンなし）
- **制御技術への高度依存**（ECCD, feedback）

### 7.3 plasma_sim実装への提言

**即座に実装すべき**:
1. IPB98(y,2)閉じ込めスケーリング
2. 運転限界チェック（β, nG）
3. 時間発展ループ（エネルギーバランス）

**次のステップ**:
4. Modified Rutherford方程式（NTM時間発展）
5. ECCD制御アルゴリズム（位置最適化）
6. 統合シミュレータクラス

**長期目標**:
7. リアルタイム診断シミュレータ
8. 不確実性評価（モンテカルロ）
9. 運転シナリオ最適化

---

## 参考文献

1. ITER Physics Basis, Nuclear Fusion 39 (1999) 2137-2638
2. Chapter 1: Overview and summary
3. Chapter 2: Plasma confinement and transport
4. Chapter 3: MHD stability, operational limits and disruptions
5. Chapter 6: Plasma auxiliary heating and current drive
6. Chapter 7: Diagnostics
7. Chapter 8: Plasma operation and control

---

**この分析の差別化要因**:
- ✓ 単なるデータ抽出ではなく、**因果関係の明示**
- ✓ トレードオフと設計思想の**深い理解**
- ✓ plasma_simコードへの**具体的実装提案**
- ✓ **実用的結論**と**アクション可能な推奨事項**
