# ITER Physics Expert Group on Confinement and Transport PDFの詳細分析レポート

## 実行日時

2026年3月2日

## 対象ファイル

`ITER_Physics_Expert_Group_on_Confinement_and_Transport_1999_Nucl._Fusion_39_2175.pdf`

---

## 1. 文書の基本情報

### 1.1 概要

- **タイトル**: Chapter 2: Plasma confinement and transport
- **著者グループ**: ITER Physics Expert Group on Confinement and Transport
- **ページ数**: 76ページ
- **掲載誌**: Nuclear Fusion, Vol. 39, No. 12 (1999)
- **引用**: Nuclear Fusion 39 2175

### 1.2 主要章・節構成

1. Introduction (2176)
2. Mechanisms of transport in a tokamak (2178)
3. Experimental description of confinement and transport (2184)
   - 3.2. General results for ohmic and L-mode
   - 3.3. Regimes with edge transport barrier (H-mode) and recommended regime for ITER
   - 3.4. Regimes with internal transport barriers
   - 3.5. Enhanced confinement with edge radiation
4. L–H and H–L transition physics (2192)
5. Impact of global instabilities on transport (2198)
6. Global energy confinement scalings (2201)
7. Scaling studies with similar dimensionless physics parameters (2209)
8. One dimensional transport models (2215)
9. Particle transport (2225)
10. Momentum confinement (2228)
11. Summary (2231)

---

## 2. プラズマプロファイルに関する記述

### 2.1 プロファイル形状の一般的記述

#### 2.1.1 基本的な輸送方程式

文書では、プロファイルの時間発展を記述する1次元輸送方程式が示されています：

```bash
∂n_a/∂t = -(1/r) ∂(rΓ_a)/∂r + S_a     (密度)
∂T_a/∂t = -(1/r) ∂(rQ_a)/∂r + P_a     (温度)
```

ここで、Γ_a（粒子束）、Q_a（熱流束）は拡散係数を用いて：

```bash
Γ_a = -D_a ∂n_a/∂r
Q_a = -χ_a ∂T_a/∂r
```

と表されます。

#### 2.1.2 ディメンションレス表現

拡散係数は次のように記述されます：

```bash
D = c_s ρ_s^β F(ρ*, ν*, q, A, κ, δ, L_T/R, L_n/R, ...)
```

- `β = 0`: Bohm scaling
- `β = 1`: gyroBohm scaling
- `ρ* = ρ_i/a`: 規格化ラーマー半径
- `c_s = √(T_e/m_i)`: 音速
- `ρ_s = √(2m_i T_e)/(eB)`: イオンラーマー半径（電子温度評価）

### 2.2 プロファイル指数の記述

**重要**: 本PDFでは具体的なプロファイル指数（α_n, α_T等）の数値は直接的には記載されていません。代わりに、以下のような記述があります：

1. **1Dトランスポートコードの検証に関する記述**（Section 8）では、輸送コードの予測能力を評価する際にプロファイル形状が議論されています。

2. **Pedestal構造の記述**（Section 3.3, 4.2）では、H-modeにおけるペデスタル幅と高さが議論されていますが、コア領域の具体的なα値は明示されていません。

3. **他の論文への参照**: 本文書は主にスケーリング則と輸送メカニズムに焦点を当てており、具体的なプロファイル指数については他の文献（特にChapter 1: Overview and summary、実験装置の個別報告等）を参照するよう示唆されています。

### 2.3 一般的に使用される値（間接的情報）

トランスポート理論と実験データから推測される典型値：

#### 密度プロファイル

- **L-mode**: やや平坦（α_n ≈ 0.5 - 1.0）
- **H-mode**: コアは平坦（α_n ≈ 0 - 0.5, "Region I"として言及）
  - "Flat density profile" の記述あり（Section 3.3）
- **Pedestal**: r/a > 0.9 で急勾配

#### 温度プロファイル

- **L-mode/H-mode**: 中程度のピーキング（α_T ≈ 1.0 - 2.0推定）
  - 文献では "parabolic" という表現が使用されている
- **先進シナリオ（Reversed Shear等）**: 強いピーキング（α_T > 2.0）

#### Te ≈ Ti の制約

- 燃焼プラズマでは電子温度とイオン温度がほぼ等しい（α粒子加熱の効果）

---

## 3. ITER標準運転シナリオのパラメータ

### 3.1 基本運転シナリオ

#### **ELMy H-mode**（ITER基本運転モード）

| パラメータ          | 値                |
| ------------------- | ----------------- |
| 小半径 a            | 2.0 m             |
| 大半径 R            | 6.2 m             |
| プラズマ電流 Ip     | 15 MA             |
| トロイダル磁場 BT   | 5.3 T             |
| 中心密度 n_e0       | ~1.0 × 10^20 m^-3 |
| 中心温度 T_e0, T_i0 | ~15 keV (燃焼相)  |
| β_N                 | ~2.5              |
| H-factor (H98(y,2)) | ~1.0              |

#### **L-mode**（低閉じ込めモード）

- 補助加熱パワーが閾値以下
- 閉じ込め時間が短い
- ペデスタル構造なし

#### **先進シナリオ**

1. **Reversed Shear (RS)**: 内部輸送障壁（ITB）を持つ
2. **Hybrid scenario**: RS と ELMy H-mode の中間
3. **Steady-state scenario**: 非帰納電流駆動

### 3.2 ELMy H-modeのプロファイル特性

#### ペデスタル構造

- **ペデスタルトップ位置**: r/a ≈ 0.9 - 0.95
- **ペデスタル幅**:
  - 密度: Δ_ne ≈ 2-3 cm（装置依存、ρ_piスケーリングの可能性）
  - 温度: Δ_Te, Δ_Ti ≈ 2-2.5 cm（ASDEX-Upgradeデータ）
- **ペデスタル高さ**:
  - 圧力勾配は理想バ ルーニング安定性限界近傍
  - DIII-Dデータ: 無限nバルーニング限界の2-3倍まで可能

#### コア領域プロファイル

- **密度**: フラット（Region I）
  - 実験: Greenwald限界以下で運転
- **温度**:
  - ピーキングあり（詳細な指数は文書に明示されず）
  - Te ≈ Ti（燃焼プラズマの特徴）

---

## 4. スケーリング則

### 4.1 エネルギー閉じ込め時間スケーリング

#### **IPB98(y)** スケーリング

```bash
τ_E = 0.0365 × I_p^0.97 × B_T^0.08 × P_heat^-0.63 × n̄_e^0.41 × M^0.19 × R^1.93 × κ^0.67 × a^0.23 × ε^0.20
```

- RMSE: 15.8%
- ITER予測: τ_E = 6.0 s

#### **IPB98(y,2)** スケーリング（推奨）

```bash
τ_E,th = 0.0562 × I_p^0.93 × B_T^0.15 × P_heat^-0.69 × n̄_e^0.41 × M^0.19 × R^1.97 × κ^0.78 × ε^0.58
```

- RMSE: 14.5%
- ITER予測: τ_E = 4.9 s
- **95%信頼区間**: τ_ITER = 4.4 - 6.8 s（狭い信頼区間）
- **保守的推定**: τ_ITER = 3.5 - 8.0 s（広い信頼区間）

#### **IPB98(y,3)** スケーリング

- Alcator C-MODを除外したデータセット
- ITER予測: τ_E = 5.0 s

### 4.2 H-mode閾値パワースケーリング

#### 一般式

```bash
P_thr = C(R/a, κ, q, α) × B_T × n̄_e^0.75 × R^2 × (n̄_e R^2)^α
```

- C = (0.45 ± 0.1) × β^0.6
- α: -0.25 < α < 0.25（データセット依存）

#### ITER予測

- **予測範囲**: P_thr ≈ 50 - 200 MW
- **不確実性の主因**: R依存性（R^1.5 〜 R^2.5）
- **実機での低減要因**:
  - Single null配置 + ion ∇B drift方向最適化 → 約2倍低減
  - 重水素 → 約2倍低減（水素比）
  - 壁調整・不純物低減 → さらなる低減

### 4.3 プロファイル形状依存性

#### Stiffness（剛性）の問題

- ITG乱流モデルでは、温度勾配が臨界値を超えると熱拡散係数が急増
- "Stiff transport"では、コア温度がエッジ温度に強く連結
- **ITER への示唆**: 比較的高いエッジ温度が必要

#### ディメンションレススケーリング

- gyroBohm scaling（β = 1）: 高閉じ込めモード（H-mode）で支持
- Bohm scaling（β = 0）: L-modeで観測例あり
- **実験**: 装置間比較（DIII-D/JET）でディメンションレス相似性確認

---

## 5. 輸送モデル

### 5.1 使用されている輸送コード

#### 主要コード

1. **TRANSP**（PPPL開発）
2. **ASTRA**（ロシア開発）
3. **JETTO**（JET開発）
4. **ONETWO**（General Atomics）

#### コードの種類

- **Predictive codes**: ソース/シンクを計算
- **Interpretive codes**: ソース/シンクをデータベースから取得

### 5.2 新古典輸送 vs 乱流輸送

#### 新古典輸送

- **適用範囲**: 平行方向（磁力線方向）輸送
- **特徴**:
  - バナナ regime: ν* < 1, 拡散係数 ∝ q² ε^(-3/2)
  - Plateau regime: 中間
  - Pfirsch-Schlüter regime: ν* > 1, 拡散係数 ∝ q²
- **実験との整合性**: 並行輸送は理論と一致
- **ブートストラップ電流**: 新古典理論で説明

#### 異常輸送（乱流輸送）

- **主因**: マイクロ不安定性による乱流
- **支配的なモード**:
  1. **ITG mode**（Ion Temperature Gradient）: コア領域
  2. **TEM**（Trapped Electron Mode）: 電子温度勾配
  3. **ETG**（Electron Temperature Gradient）: 短波長モード
  4. **Resistive ballooning**: エッジ領域

#### 混合長推定

```bash
D_turb ~ γ/k_⊥²
```

ここで、γ: 成長率、k_⊥: 垂直波数

### 5.3 E×B流シアによる乱流抑制

#### メカニズム

- E×B速度のシア（半径方向変化）が乱流を decorrelate
- **実験的証拠**: シア増大と乱流抑制の因果関係確認（Section 4.1）
- **理論**: 線形安定化ではなく、非線形飽和レベルの低減

#### 応用

- H-mode遷移の説明
- 内部輸送障壁（ITB）の形成メカニズム

### 5.4 温度・密度プロファイルの決定メカニズム

#### プロファイル剛性（Profile Resilience）

- プロファイルは外部擾乱に対して一定の形状を維持する傾向
- 「Self-organized criticality」の可能性

#### 周辺条件の重要性

- コアプロファイルはペデスタル構造に強く依存
- Stiff ITG モデル: T_edge → T_core の強い結合

#### 予測の課題

- エッジ領域（0.9 < r/a < 1）のモデル化が不十分
- 1Dコードの境界条件感度が高い

---

## 6. plasma_sim_ech_enhanced.pyへの応用

### 6.1 現在のコード設定

#### ITER設定（plasma_sim_ech_enhanced.py内）

```python
"ITER": {
    "a": 2.0,           # 小半径 [m]
    "B0": 5.3,          # 中心磁場 [T]
    "n0": 1.0e20,       # 中心密度 [m^-3]
    "T0": 15e3,         # 中心温度 [eV]
    "freq": 170e9,      # ECH周波数 [Hz]
}

# 現在のプロファイル
B_profile = B0 * (1 - 0.8 * (r/a)^2) + 0.1
n_profile = n0 * (1 - (r/a)^2)^2 + 1e17      # α_n = 2
T_profile = T0 * (1 - (r/a)^2)^1.5 + 100     # α_T = 1.5
```

### 6.2 プロファイル設定の妥当性評価

#### 密度プロファイル

**現在**: `n(r) = n0 * (1 - (r/a)²)² + 1e17`（α_n = 2）

**分析結果**:

- ✗ **過度にピーキング**: ITER  Physics Basisでは「flat density profile（Region I）」と記述
- **推奨改善**: `n(r) = n0 * (1 - (r/a)²)^0.5`程度（α_n ≈ 0.5 - 1.0）
- **または**: ペデスタル構造を考慮した2領域モデル

  ```python
  # r/a < 0.9: フラット
  n_core = n0 * (1 - 0.1 * (r/a)^2)
  # r/a > 0.9: ペデスタル
  n_edge = pedestal model
  ```

#### 温度プロファイル

**現在**: `T(r) = T0 * (1 - (r/a)²)^1.5 + 100`（α_T = 1.5）

**分析結果**:

- ✓ **妥当**: 1.0 < α_T < 2.0 の範囲は合理的
- ✓ parabolic形状は一般的
- **改善の余地**: 
  1. ペデスタル構造の追加（r/a > 0.9）
  2. ITBシナリオでは α_T > 2.0 も考慮

#### 磁場プロファイル

**現在**: `B(r) = B0 * (1 - 0.8 * (r/a)²) + 0.1`

**分析結果**:

- ✓ **妥当**: Grad-Shafranov平衡の近似として合理的
- **注意**: 実機では Shafranov shift により R方向に非対称

### 6.3 推奨される改善

#### 改善案1: ペデスタル構造の追加

```python
def enhanced_density_profile(r, a, n0, n_ped, r_ped=0.9*a, width=0.05*a):
    """ペデスタル構造付き密度プロファイル"""
    n_core = n0  # フラットコア
    n_pedestal = n_ped * np.exp(-((r - r_ped)/width)**2)  # ガウシアンペデスタル
    return n_core + n_pedestal

def enhanced_temperature_profile(r, a, T0, T_ped, alpha_T=1.5):
    """ペデスタル構造付き温度プロファイル"""
    # コア領域
    T_core = T0 * (1 - (r/a)**2)**alpha_T
    
    # ペデスタル (simplified)
    if r/a > 0.9:
        T_pedestal = T_ped
    else:
        T_pedestal = T_core
    
    return max(T_core, T_pedestal) + 100  # 最低温度100 eV
```

#### 改善案2: シナリオ依存のプロファイル

```python
PROFILE_CONFIGS = {
    "H-mode": {
        "alpha_n": 0.5,   # Flat core
        "alpha_T": 1.5,   # Moderate peaking
        "pedestal": True,
    },
    "L-mode": {
        "alpha_n": 1.0,
        "alpha_T": 1.0,
        "pedestal": False,
    },
    "RS-ITB": {
        "alpha_n": 1.5,
        "alpha_T": 2.5,   # Strong peaking
        "pedestal": True,
        "ITB_location": 0.5,  # r/a
    },
}
```

### 6.4 ECH関連パラメータの検証

#### 周波数設定

- **現在**: 170 GHz
- **ITER計画**: 170 GHz（24 MW × 24）, 2nd harmonic X-mode
- ✓ **妥当**

#### 相対論的補正

```python
# 現在の実装
gamma = √(1 + T_eV * e / (m_e * c²))
f_ce_relativistic = f_ce_classical / gamma
```

- ✓ **正しい実装**: T_e ~ 15 keV → γ ≈ 1.03（約3%補正）

#### カットオフ条件

- O-mode: f > f_pe
- X-mode: f > f_R,L
- ✓ **実装済み**

### 6.5 スケーリング検証の推奨項目

#### 1. パラメータスキャン

- 密度スキャン: n_e = 0.5~1.5 × 10^20 m^-3
- 温度スキャン: T_e = 10~20 keV
- 磁場スキャン: B_T = 4~6 T

#### 2. ディメンションレス比較

- JT-60SA等の既存装置との ρ* スケーリング検証
- gyroBohm vs Bohm の検証

#### 3. プロファイル形状の感度解析

- α_n, α_T の変化が吸収分布に与える影響

---

## 7. まとめと結論

### 7.1 主要な発見

1. **プロファイル指数の直接的記述なし**
   - 本PDFでは具体的なα値は明示されていない
   - 「flat density」「parabolic temperature」等の定性的記述のみ

2. **間接的情報からの推定**
   - 密度: α_n ≈ 0.5 - 1.0（H-mode core）
   - 温度: α_T ≈ 1.0 - 2.0（通常運転）
   - ペデスタル構造が重要

3. **スケーリング則の詳細データ**
   - IPB98(y,2): τ_E,ITER = 4.9 s（4.4-6.8 s信頼区間）
   - H-mode閾値: 50-200 MW（不確実性大）

4. **輸送メカニズム**
   - ITG乱流が支配的
   - E×B流シアによる抑制が鍵
   - Stiffness問題

### 7.2 plasma_sim_ech_enhanced.pyへの適用

#### 推奨される変更

1. **密度プロファイル**: α_n = 2 → 0.5~1.0
2. **ペデスタル追加**: r/a > 0.9 に急勾配領域
3. **シナリオ切り替え**: H-mode/L-mode/ITBの選択機能

#### 現状で妥当な点

- 温度プロファイル: α_T = 1.5 ✓
- ECH周波数: 170 GHz ✓
- 相対論的補正: 実装済み ✓
- 基本パラメータ: 妥当 ✓

### 7.3 今後の推奨アクション

1. **より詳細なプロファイルデータの取得**
   - ITER Physics Basis Chapter 1（Overview）
   - 個別実験装置の論文（JT-60U, JET等）
   - Doyle et al., Nucl. Fusion 47 (2007) S18（プロファイルレビュー）

2. **ペデスタル物理の実装**
   - Chapter 3（MHD）、Chapter 4（Divertorとペデスタル）の参照

3. **輸送コードとの比較**
   - TRANSP, ASTRAの出力データと比較

4. **シミュレーション拡張**
   - 多周波数ECHシステム
   - 電流駆動（ECCD）の評価
   - ELMの影響検討

---

## 参考文献（PDF内で引用）

1. ITER Physics Basis (1999), Nuclear Fusion 39, 2137-2664
2. IPB98(y,2) scaling: Section 6.3
3. H-mode threshold: Section 4.3
4. Transport models: Section 8
5. Dimensionless scaling: Section 7

---

## 付録: 数値まとめ

### ITERパラメータ（ELMy H-mode）

| 項目              | 値             | 単位 |
| ----------------- | -------------- | ---- |
| 小半径 a          | 2.0            | m    |
| 大半径 R          | 6.2            | m    |
| 縦長比 κ          | 1.7            | -    |
| 三角度 δ          | 0.33           | -    |
| プラズマ電流 Ip   | 15             | MA   |
| トロイダル磁場 BT | 5.3            | T    |
| 線平均密度 n̄_e    | ~1.0 × 10^20   | m^-3 |
| 中心温度 T0       | ~15            | keV  |
| 閉じ込め時間 τ_E  | 4.9 (4.4-6.8)  | s    |
| H-factor H98(y,2) | ~1.0           | -    |
| 規格化β β_N       | ~2.5           | -    |
| 安全係数 q95      | ~3.0           | -    |
| ECH周波数         | 170            | GHz  |
| ECH電力           | 24 × 1 MW = 24 | MW   |

### 推奨プロファイル指数

| プロファイル     | 推奨α値   | 現在の実装  | 評価   |
| ---------------- | --------- | ----------- | ------ |
| 密度 n(r)        | 0.5 - 1.0 | 2.0         | 要改善 |
| 電子温度 Te(r)   | 1.0 - 2.0 | 1.5         | 妥当   |
| イオン温度 Ti(r) | 1.0 - 2.0 | (Te=Ti仮定) | 妥当   |

---

以上
