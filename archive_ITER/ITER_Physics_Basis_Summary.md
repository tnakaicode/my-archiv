# ITER Physics Basis (1999) - 詳細分析レポート

**PDFファイル:** `ITER_Physics_Basis_Editors_1999_Nucl._Fusion_39_2137.pdf`  
**分析日:** 2026年3月2日  
**関連コード:** `plasma_sim_ech_enhanced.py`

---

## 1. 論文の基本情報

### 書誌情報

- **タイトル:** Chapter 1: Overview and summary (ITER Physics Basis)
- **著者/編集者:** ITER Physics Basis Editors
  - ITER Physics Expert Group Chairs and Co-Chairs
  - ITER Joint Central Team and Physics Integration Unit
- **出版年:** 1999
- **ジャーナル:** Nuclear Fusion, Vol. 39, No. 12, pp. 2137-2174
- **DOI:** (PDFから完全なDOI情報は抽出できませんでしたが、引用情報は確認できました)
- **総ページ数:** 39ページ

### 編集者

- **Physics Basis Editors:** F.W. Perkins (ITER JCT), D.E. Post (ITER JCT), N.A. Uckan (ORNL), M. Azumi (JAERI), D.J. Campbell (NET), N. Ivanov (RRC-Kurchatov), N.R. Sauthoff (PPPL), M. Wakatani (Kyoto Univ.)

---

## 2. 論文の目的と概要

### 目的

ITER Physics Basisは、核融合エネルギーの科学的・技術的実現可能性を実証するための**トカマク燃焼プラズマ装置の設計基盤**となる物理規則と方法論を提示・評価することを目的としています。

### ITERプロジェクトにおける位置づけ

- **ITER EDA (Engineering Design Activities) の物理的基盤文書**
- 燃焼プラズマ実験の設計要件を定義
- 1000秒以上にわたり**核融合加熱が輸送損失と放射損失とバランスする（または同等である）**燃焼プラズマ施設の実現可能性を科学的に裏付ける

### 主要な目標

> "To demonstrate the scientific and technological feasibility of fusion energy for peaceful purposes"

---

## 3. 主要な章構成

### 目次（Contents）

本文書は以下のような構成となっています：

1. **Introduction** (p. 2138)
2. **ITER** (p. 2139)
   - 2.1 ITER: background and mandate
   - 2.2 ITER: FDR design
3. **Tokamak physics processes and projection principles** (p. 2142)
   - 3.1 General projection issues
   - 3.2 Core confinement and transport
     - 3.2.1 Global confinement scaling
     - 3.2.2 H-mode power threshold and pedestal
     - 3.2.3 Transport modelling and simulation
     - 3.2.4 Confinement and magnetic configuration
   - 3.3 Magnetohydrodynamic phenomena, disruptions and operational limits
   - 3.4 Particle control and power dispersal
   - 3.5 Energetic particle physics
   - 3.6 **Auxiliary power physics**
   - 3.7 Physics of plasma diagnostics
   - 3.8 Physics of plasma control and steady state operation
   - 3.9 Summary
4. **Reactor scale experimental plasma physics** (p. 2161)
5. **Projecting ITER operations** (p. 2164)
6. **Concluding remarks** (p. 2166)
7. **Appendices**

---

## 4. 主要な物理パラメータ

### ITER FDR設計パラメータ（Table 1）

Reference ignited ELMy H-mode operation

| パラメータ                       | 値                     | 備考                         |
| -------------------------------- | ---------------------- | ---------------------------- |
| **Major radius (R)**             | 8.14 m                 | 主半径                       |
| **Minor radius (a)**             | 2.80 m                 | 小半径                       |
| **Plasma configuration**         | Single null divertor   | 単一ヌルダイバータ           |
| **Vertical elongation**          | 1.6                    | (at 95% poloidal flux)       |
| **Triangularity**                | 0.24                   | (at 95% poloidal flux)       |
| **Plasma volume**                | 2000 m³                |                              |
| **Plasma surface area**          | 1200 m²                |                              |
| **Nominal plasma current (Ip)**  | 21 MA                  | プラズマ電流                 |
| **Electron density (ne)**        | 0.98×10²⁰ m⁻³          | 電子密度                     |
| **Volume average temperature**   | 12.9 keV               | 体積平均温度                 |
| **Toroidal field (BT)**          | 5.68 T                 | トロイダル磁場 (at R=8.14 m) |
| **MHD safety factor (q95)**      | 3.0                    | (at 21 MA)                   |
| **Volume average β / βN**        | 0.030 / 2.29           | 規格化ベータ                 |
| **Fusion power (ignited)**       | 1.5 GW                 | 核融合出力                   |
| **Plasma thermal energy**        | 1.07 GJ                | プラズマ熱エネルギー         |
| **Plasma magnetic energy**       | 1.1 GJ                 | プラズマ磁気エネルギー       |
| **Confinement mode**             | ELMy H-mode            | 閉じ込めモード               |
| **Radiation from core**          | 118 MW                 | コア放射                     |
| **Transport power loss**         | 182 MW                 | 輸送損失                     |
| **Energy confinement time (τE)** | 5.9 s                  | エネルギー閉じ込め時間       |
| **Ptransport/PL→H**              | 1.4                    | H-mode遷移閾値との比         |
| **Species concentrations**       | He/Be/Ar: 10%/2%/0.16% | 組成                         |
| **Zeff**                         | 1.9                    | 実効電荷                     |
| **Neutron wall loading**         | 1 MW/m²                | (at 1.5 GW)                  |
| **Lifetime neutron fluence**     | 1 MWa/m²               |                              |
| **Burn duration (ignited)**      | 1000 s                 | 燃焼時間（誘導電流駆動）     |
| **Auxiliary heating power**      | 100-150 MW             | 補助加熱パワー範囲           |
| **In vessel tritium inventory**  | 1 kg                   | 安全上限                     |

### その他の運転パラメータ（記載例）

- **Plasma current (I):** 2.0 MA (in smaller device examples)
- **Major radius (R):** 2.9 m (in smaller device examples)
- **Minor radius (a):** 0.93 m (in smaller device examples)
- **Auxiliary heating power:** 17.3 MW (in example scenario)
- **Magnetic field:** JETでは3.8 T、ITERでは5.68 T

---

## 5. ECH（Electron Cyclotron Heating）関連の記述

### 検出された情報

- **"ECH" の出現回数:** 51箇所
- **"electron cyclotron" の出現回数:** 2箇所
- **"ECRH" の出現回数:** 0箇所（この用語は使用されていない）

### 補助加熱システム

文書中に以下の記述があります：

> "Auxiliary heating power in the range 50–150 MW can take the form of:
> **Negative ion based 1 MeV neutral beam injection**
> **Ion cyclotron heating** by the fast magnetosonic Alfvén wave
> **Electron cyclotron heating**"

### ECHの役割と特徴

1. **電流駆動能力（Current Drive Capability）**
   - ECHシステムは電流駆動能力を有する
   - **電流分布制御（current profile control）**に利用可能
   - "electron cyclotron heating is notable in that its current drive can be utilized for current prole control"

2. **Neoclassical Tearing Mode（NTM）の制御**
   - "permits stabilization via **electron cyclotron current drive**" [参考文献 40, 41]
   - ネオクラシカルテアリングモードの安定化にECCDが有効

3. **現状の課題**
   - "At present, ECH is under-utilized in contemporary tokamaks because **reliable sources are only just now becoming available**"
   - 1999年時点では、ECHソースの信頼性向上が課題
   - 中性粒子ビーム並みのパワーレベルで実証されるには5-10年必要と予測

### 具体的な周波数・パワー情報

**残念ながら、この文書（Chapter 1: Overview）には以下の詳細は記載されていません：**

- ECHの具体的な周波数（例: 170 GHz）
- ジャイロトロンのパワー
- ECH用ミラー系の詳細

これらの情報は、**Chapter 6（Auxiliary power physics）や他の技術文書**に記載されている可能性が高いです。

---

## 6. プロファイルに関する記述

### 密度プロファイル (Density Profile)

Figure 2に対応する記述：
> "Because there is essentially **no ionization occurring inside the separatrix**, the **density profile is flat**. Any density gradient close to the separatrix would be sensitive to details of fuelling and not essential to performance calculations."

**重要な特徴：**

- セパラトリクス内部では**電離がほぼ発生しない**ため、密度プロファイルは**フラット**
- セパラトリクス付近の密度勾配は燃料供給の詳細に依存
- コア性能計算には本質的でない

### 温度プロファイル (Temperature Profile)

> "Ion temperature profile (keV) corresponding to the plasma of Table 1. **Electron and ion temperatures are close to equal.**"

**重要な特徴：**

1. **Te ≈ Ti（電子温度 ≈ イオン温度）**
   - 燃焼プラズマでは電子・イオン温度がほぼ等しい
   - アルファ粒子が主に電子を加熱するため
   - 温度緩和時間（τeq ≈ 0.5 s）がエネルギー閉じ込め時間（τE ≈ 6 s）より短い

2. **現在の実験装置との違い**
   - 現在の実験では Ti > Te が実現可能
   - ビーム加熱が主にイオンを加熱
   - τeq ≈ τE のため、温度差を維持できる
   - しかし**燃焼プラズマでは Ti ≈ Te が制約条件**

### プロファイルモデリング

文書中には以下の記述があります：

1. **磁気面モデル（Magnetic Surface Model）**
   > "The very rapid transport of heat and particles along a magnetic surface relative to the slow transport across surfaces has lead to a model of plasma transport wherein **magnetic surfaces are regarded as iso-density, iso-temperature surfaces**"

2. **1.5次元輸送モデル（1.5 Dimensional Transport Model）**
   - 磁気面を等密度・等温度面とみなす
   - 磁気面を横切る輸送のみを計算
   - 磁気面の形状全体を体積要素の定義に使用

3. **Pedestal（ペデスタル）**
   - H-mode運転では**edge pedestal**が重要
   - "Pedestal values of density and temperature just inside the separatrix"
   - Pedestal温度がコア温度プロファイルに影響を与える可能性

4. **Internal Transport Barriers (ITBs)**
   - 図7にJT-60Uの例が示されている
   - 逆シア配位で観測される内部輸送障壁
   - Te, Ti, ne プロファイルが急峻な勾配を持つ

### プロファイル指数（Profile Exponents）

**残念ながら、この文書には以下の具体的な数値は明記されていません：**

- 密度プロファイル指数 α_n
- 温度プロファイル指数 α_T
- 具体的なプロファイル関数形（例: n(r) = n0(1-(r/a)²)^α）

これらの詳細は**Chapter 2（Core confinement and transport）**や**ITER Profile Database**に記載されている可能性があります。

### プロファイルに関する追加情報

- **Flat density profile in Region I（領域Iでのフラット密度プロファイル）**が標準
- **Temperature profile will determine the off-axis current drive profile**（温度プロファイルがオフアクシス電流駆動プロファイルを決定）
- Lower hybrid current driveでは、密度プロファイルがフラットと予想されるため、温度プロファイルが重要

---

## 7. 重要な結論・知見

### 7.1 燃焼プラズマの実現可能性

1. **ITER FDRは燃焼プラズマ実験として適切なスケール**
   - JETのDT ELMy H-mode放電と比較して：
     - 磁場強度：1.5倍
     - 線形サイズ：2.9倍
   - Fusion figure of merit M = nDT(0)·Ti(0)·τE において、ITERは現在の実験の約40倍

2. **点火条件（Ignition Condition）**
   - M ≥ 110 が点火の最小条件
   - ITER FDRパラメータはこの条件を満たす

### 7.2 物理プロセスの統合

> "Since each physics element has its own scaling properties, an **integrated experimental demonstration** of the balance between the combined processes which obtains in a reactor plasma is **inaccessible to contemporary experimental facilities: it requires a reactor scale device.**"

- 各物理要素が独自のスケーリング特性を持つ
- 炉レベルプラズマでの統合実証は現在の実験装置では不可能
- **炉スケール装置が必要**

### 7.3 運転モード

1. **Inductive (Pulsed) Mode（誘導（パルス）モード）**
   - 電流を誘導的に駆動
   - 燃焼時間：1000秒

2. **Steady State Mode（定常モード）**
   - Non-inductive plasma current drive（非誘導電流駆動）
   - Lower hybrid current drive, ECCD, neutral beam current drive

### 7.4 主要な物理課題

1. **Confinement（閉じ込め）**
   - Global confinement scaling（ELMy H-mode scalingなど）
   - H-mode power threshold and pedestal physics
   - Internal transport barriers (ITBs)

2. **MHD Stability（MHD安定性）**
   - βN限界（ネオクラシカルテアリングモードが制約）
   - Disruptions and VDEs（破壊現象と垂直移動現象）
   - ELMs（エッジ局在化モード）
   - Sawteeth（ソーティース振動）

3. **Divertor Physics（ダイバータ物理）**
   - Power dispersal（熱負荷分散）
   - Helium exhaust（ヘリウム排気）
   - Erosion and tritium retention（侵食とトリチウム蓄積）

4. **Energetic Particle Physics（高エネルギー粒子物理）**
   - Alpha particle confinement（アルファ粒子閉じ込め）
   - Alpha heating（アルファ加熱）

5. **Auxiliary Power Physics（補助加熱物理）**
   - NBI, ICRH, ECH, LH current drive
   - Current profile control

### 7.5 不確実性とリスク

> "For each design, there will remain a **significant uncertainty** in the projected performance, but the projection methodologies outlined here do suffice to specify the major parameters of such a facility."

- 設計された性能には**有意な不確実性が残る**
- しかし、投影方法論は主要パラメータを特定するのに十分
- 段階的運転により、商用核融合炉プロトタイプ設計に必要な情報を取得可能

---

## 8. plasma_sim_ech_enhanced.py コード検証への示唆

### 8.1 適用すべきITERパラメータ

コード検証のため、以下のITER FDRパラメータを使用することを推奨：

```python
# ITER FDR Parameters
B0 = 5.68          # Toroidal field at R0 [T]
R0 = 8.14          # Major radius [m]
a = 2.80           # Minor radius [m]
Ip = 21e6          # Plasma current [A]
ne_avg = 0.98e20   # Average electron density [m^-3]
Te_avg = 12.9e3    # Average temperature [eV] (12.9 keV)
```

### 8.2 プロファイルモデル

ITER Physics Basisに基づくと：

1. **密度プロファイル：フラット**

   ```python
   # Flat density profile (Region I)
   n_e(r) = n_e0 = const  (for r/a < 0.9)
   ```

2. **温度プロファイル：ピーキング**

   ```python
   # Temperature profile (要確認：具体的なα値は本文書に記載なし)
   # 一般的な形状から推定：
   T_e(r) = T_e0 * (1 - (r/a)^2)^α_T
   # α_T ≈ 1.5-2.0 程度が妥当（要詳細確認）
   ```

3. **Te ≈ Ti の条件**
   - 燃焼プラズマでは電子温度とイオン温度がほぼ等しい
   - コードでこの条件を考慮する必要がある

### 8.3 ECH関連パラメータ

- **ECH周波数：** 具体的な値は本文書に記載なし（別文書で確認必要）
- **ECHパワー：** 100-150 MW（全補助加熱）のうち一部
- **ECHの役割：**
  - 電流分布制御（Current profile control）
  - ネオクラシカルテアリングモード安定化

### 8.4 検証すべき物理過程

1. **サイクロトロン共鳴吸収（Cyclotron Resonance Absorption）**
   - 基本波（ω = ωce）と第2高調波（ω = 2ωce）
   - 相対論的補正（γ因子）の重要性

2. **偏光モード（O-mode / X-mode）**
   - カットオフ条件の確認
   - 最適な偏光モードの選択

3. **Ray Tracing**
   - "Because both the frequency and parallel wavenumber are fixed..."
   - ITER規模では**single-pass absorption**が期待される（小型装置では**multi-pass**）

### 8.5 スケーリングの検証

コードが以下のスケーリングを正しく再現できているか確認：

- サイズ（linear dimension）：×2.9 (JET → ITER)
- 磁場（magnetic field）：×1.5
- プラズマ電流（plasma current）：×3-4

---

## 9. 追加調査が必要な項目

### 本文書（Chapter 1）に記載されていない情報

以下の詳細情報は、ITER Physics Basis の**他の章**を参照する必要があります：

1. **Chapter 2: Confinement and Transport**
   - プロファイル指数の具体的な値（α_n, α_T）
   - ITER Profile Database
   - Transport coefficient models

2. **Chapter 6: Auxiliary Power Physics**
   - ECHの具体的な周波数（170 GHz?）
   - ジャイロトロン仕様（パワー、台数）
   - ECH伝送系の詳細
   - Ray tracing計算の詳細

3. **Chapter 3: MHD Stability**
   - q-profileの詳細
   - Current profile requirements

4. **Chapter 4: Divertor and Edge Physics**
   - Pedestal構造の詳細
   - Edge density/temperature profiles

### 推奨される追加文献

- ITER Final Design Report (FDR)関連文書
- ITER Physics Basis Chapter 6 (ECH/CD専門chapter)
- ITER Technical Basis (IAEA Technical Report Series)

---

## 10. まとめと結論

### 主要な発見

1. **ITER FDRの設計は1999年時点で明確に定義されている**
   - 主要なプラズマパラメータが包括的に記載
   - R/a = 8.14/2.80 m, Ip = 21 MA, BT = 5.68 T

2. **ECHはITERの補助加熱・電流駆動システムの重要な要素**
   - 100-150 MWの補助加熱のうち一部を担う
   - 電流分布制御に特に有用
   - NTM安定化の可能性

3. **プロファイルの特徴**
   - 密度：フラット（Region I）
   - 温度：Te ≈ Ti（燃焼プラズマの制約）
   - Pedestal構造が重要

4. **コード検証への適用可能性**
   - `plasma_sim_ech_enhanced.py`の検証に必要な主要パラメータは入手可能
   - ECH周波数などの詳細は別文書で確認必要
   - ITER条件での相対論的補正、カットオフ条件の検証が可能

### 次のステップ

1. ITER Physics Basis **Chapter 6** (Auxiliary Power Physics)の入手・分析
2. 具体的なECH周波数・パワー・ビーム配置の確認
3. プロファイル指数α値の確定（Chapter 2 or Profile Database）
4. コードでのITERパラメータシミュレーション実行

---

**分析完了日:** 2026年3月2日  
**分析者:** GitHub Copilot  
